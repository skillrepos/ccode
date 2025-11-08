#!/usr/bin/env python3
"""
API Tester Script

A utility script for testing REST API endpoints, validating responses,
and generating formatted test results.

Usage:
    python test-api.py <url> [--method METHOD] [--data JSON] [--headers JSON]
    python test-api.py <url> --method POST --data '{"key":"value"}'
    python test-api.py https://api.example.com/users --method GET

Options:
    --method        HTTP method (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS)
    --data          Request body as JSON string
    --headers       Additional headers as JSON string
    --auth          Authorization token or API key
    --timeout       Request timeout in seconds (default: 10)
    --verbose       Enable verbose output
    --output        Output format (json, yaml, text)
"""

import sys
import json
import argparse
from typing import Dict, Any, Optional, Tuple
from datetime import datetime
import time

try:
    import requests
    from requests.auth import HTTPBasicAuth
except ImportError:
    print("Error: 'requests' library not found.")
    print("Install with: pip install requests")
    sys.exit(1)


class APITester:
    """Test REST API endpoints and validate responses."""

    def __init__(self, url: str, method: str = "GET", timeout: int = 10, verbose: bool = False):
        """
        Initialize API tester.

        Args:
            url: API endpoint URL
            method: HTTP method (GET, POST, etc.)
            timeout: Request timeout in seconds
            verbose: Enable verbose output
        """
        self.url = url
        self.method = method.upper()
        self.timeout = timeout
        self.verbose = verbose
        self.results = {
            "timestamp": datetime.now().isoformat(),
            "url": url,
            "method": method,
            "request": {},
            "response": {},
            "validation": {},
            "errors": [],
        }

    def log(self, message: str, level: str = "info") -> None:
        """Log a message if verbose mode is enabled."""
        if self.verbose:
            timestamp = datetime.now().strftime("%H:%M:%S")
            prefix = f"[{timestamp}] [{level.upper()}]"
            print(f"{prefix} {message}", file=sys.stderr)

    def validate_url(self) -> bool:
        """Validate that URL is properly formatted."""
        if not self.url.startswith(("http://", "https://")):
            self.results["errors"].append("URL must start with http:// or https://")
            return False

        if " " in self.url:
            self.results["errors"].append("URL contains spaces")
            return False

        return True

    def validate_method(self) -> bool:
        """Validate that HTTP method is supported."""
        valid_methods = {"GET", "POST", "PUT", "PATCH", "DELETE", "HEAD", "OPTIONS"}
        if self.method not in valid_methods:
            self.results["errors"].append(
                f"Invalid HTTP method '{self.method}'. Must be one of: {', '.join(valid_methods)}"
            )
            return False
        return True

    def parse_json_string(self, json_str: str) -> Optional[Dict[str, Any]]:
        """
        Parse JSON string safely.

        Args:
            json_str: JSON string to parse

        Returns:
            Parsed JSON object or None if invalid
        """
        try:
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            error_msg = f"Invalid JSON: {str(e)}"
            self.results["errors"].append(error_msg)
            self.log(error_msg, "error")
            return None

    def make_request(
        self,
        data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth_token: Optional[str] = None,
    ) -> Tuple[bool, Optional[requests.Response]]:
        """
        Make HTTP request to API endpoint.

        Args:
            data: Request body as dictionary
            headers: Additional headers
            auth_token: Bearer token or API key

        Returns:
            Tuple of (success, response)
        """
        try:
            # Prepare headers
            req_headers = headers or {}
            if auth_token:
                req_headers["Authorization"] = f"Bearer {auth_token}"

            self.log(f"Making {self.method} request to {self.url}")
            if self.verbose and data:
                self.log(f"Request body: {json.dumps(data)}")
            if self.verbose and headers:
                self.log(f"Headers: {json.dumps(headers)}")

            # Make request
            response = requests.request(
                method=self.method,
                url=self.url,
                json=data if self.method in {"POST", "PUT", "PATCH"} else None,
                headers=req_headers,
                timeout=self.timeout,
                allow_redirects=True,
            )

            # Store request details
            self.results["request"] = {
                "method": self.method,
                "url": self.url,
                "headers": dict(response.request.headers),
                "body": data,
            }

            self.log(f"Response status: {response.status_code}")
            return True, response

        except requests.exceptions.Timeout:
            error_msg = f"Request timeout after {self.timeout} seconds"
            self.results["errors"].append(error_msg)
            self.log(error_msg, "error")
            return False, None

        except requests.exceptions.ConnectionError as e:
            error_msg = f"Connection error: {str(e)}"
            self.results["errors"].append(error_msg)
            self.log(error_msg, "error")
            return False, None

        except requests.exceptions.RequestException as e:
            error_msg = f"Request error: {str(e)}"
            self.results["errors"].append(error_msg)
            self.log(error_msg, "error")
            return False, None

    def extract_response_data(self, response: requests.Response) -> Dict[str, Any]:
        """
        Extract and parse response data.

        Args:
            response: Response object

        Returns:
            Dictionary with response details
        """
        response_data = {
            "status_code": response.status_code,
            "status_text": response.reason,
            "headers": dict(response.headers),
            "content_length": len(response.content),
            "elapsed_time_ms": response.elapsed.total_seconds() * 1000,
        }

        # Try to parse response body
        try:
            if response.text:
                # Try JSON first
                response_data["body"] = response.json()
                response_data["content_type"] = "application/json"
            else:
                response_data["body"] = None
                response_data["content_type"] = response.headers.get("content-type", "text/plain")
        except json.JSONDecodeError:
            response_data["body"] = response.text[:500]  # Limit text output
            response_data["content_type"] = response.headers.get("content-type", "text/plain")
            response_data["body_truncated"] = len(response.text) > 500

        return response_data

    def validate_response(self, response: requests.Response) -> Dict[str, Any]:
        """
        Validate response structure and content.

        Args:
            response: Response object

        Returns:
            Dictionary with validation results
        """
        validation = {
            "is_success": 200 <= response.status_code < 300,
            "is_json": False,
            "is_valid_json": False,
            "has_content": len(response.content) > 0,
            "checks": [],
        }

        # Check content type
        content_type = response.headers.get("content-type", "").lower()
        validation["is_json"] = "application/json" in content_type

        # Try to parse JSON
        if validation["is_json"]:
            try:
                response.json()
                validation["is_valid_json"] = True
                validation["checks"].append(
                    {"check": "Valid JSON", "passed": True, "message": "Response is valid JSON"}
                )
            except json.JSONDecodeError as e:
                validation["is_valid_json"] = False
                validation["checks"].append(
                    {
                        "check": "Valid JSON",
                        "passed": False,
                        "message": f"Invalid JSON: {str(e)}",
                    }
                )
        else:
            validation["checks"].append(
                {
                    "check": "JSON Content-Type",
                    "passed": False,
                    "message": f"Content-Type is {content_type}, not application/json",
                }
            )

        # Check status code ranges
        status_code = response.status_code
        if 200 <= status_code < 300:
            validation["checks"].append(
                {
                    "check": "Status 2xx Success",
                    "passed": True,
                    "message": f"Status {status_code} indicates success",
                }
            )
        elif 400 <= status_code < 500:
            validation["checks"].append(
                {
                    "check": "Status 4xx Client Error",
                    "passed": False,
                    "message": f"Status {status_code} indicates client error",
                }
            )
        elif 500 <= status_code < 600:
            validation["checks"].append(
                {
                    "check": "Status 5xx Server Error",
                    "passed": False,
                    "message": f"Status {status_code} indicates server error",
                }
            )

        # Check response headers
        if response.headers.get("content-length"):
            validation["checks"].append(
                {
                    "check": "Content-Length Header",
                    "passed": True,
                    "message": f"Content-Length: {response.headers.get('content-length')} bytes",
                }
            )

        if response.headers.get("content-type"):
            validation["checks"].append(
                {
                    "check": "Content-Type Header",
                    "passed": True,
                    "message": f"Content-Type: {response.headers.get('content-type')}",
                }
            )

        if response.headers.get("server"):
            validation["checks"].append(
                {
                    "check": "Server Header",
                    "passed": True,
                    "message": f"Server: {response.headers.get('server')}",
                }
            )

        return validation

    def test(
        self,
        data: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        auth_token: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Execute API test.

        Args:
            data: Request body
            headers: Additional headers
            auth_token: Bearer token or API key

        Returns:
            Test results dictionary
        """
        self.log("Starting API test")

        # Validate input
        if not self.validate_url():
            return self.results

        if not self.validate_method():
            return self.results

        # Make request
        success, response = self.make_request(data, headers, auth_token)
        if not success or response is None:
            return self.results

        # Extract response data
        self.results["response"] = self.extract_response_data(response)

        # Validate response
        self.results["validation"] = self.validate_response(response)

        self.log("API test completed successfully")
        return self.results

    def format_text(self) -> str:
        """Format results as plain text."""
        lines = []
        lines.append("=" * 80)
        lines.append(f"API TEST RESULTS - {self.results['timestamp']}")
        lines.append("=" * 80)
        lines.append("")

        # Request info
        lines.append("📋 REQUEST")
        lines.append("-" * 80)
        lines.append(f"Method: {self.results['request'].get('method', 'N/A')}")
        lines.append(f"URL:    {self.results['request'].get('url', 'N/A')}")
        if self.results["request"].get("body"):
            lines.append(f"Body:   {json.dumps(self.results['request']['body'], indent=2)}")
        lines.append("")

        # Response info
        response = self.results["response"]
        lines.append("📦 RESPONSE")
        lines.append("-" * 80)
        status = response.get("status_code", "N/A")
        reason = response.get("status_text", "")
        lines.append(f"Status:       {status} {reason}")
        lines.append(f"Content-Type: {response.get('content_type', 'N/A')}")
        lines.append(f"Content-Length: {response.get('content_length', 'N/A')} bytes")
        lines.append(f"Response Time: {response.get('elapsed_time_ms', 0):.2f}ms")

        if response.get("body"):
            lines.append("Body:")
            if isinstance(response["body"], dict):
                lines.append(json.dumps(response["body"], indent=2))
            else:
                lines.append(str(response["body"][:200]))
        lines.append("")

        # Validation results
        validation = self.results["validation"]
        lines.append("✅ VALIDATION")
        lines.append("-" * 80)
        lines.append(f"Is Success (2xx):  {'✅ Yes' if validation.get('is_success') else '❌ No'}")
        lines.append(f"Is JSON:           {'✅ Yes' if validation.get('is_json') else '❌ No'}")
        lines.append(f"Valid JSON:        {'✅ Yes' if validation.get('is_valid_json') else '❌ No'}")
        lines.append(f"Has Content:       {'✅ Yes' if validation.get('has_content') else '❌ No'}")
        lines.append("")

        if validation.get("checks"):
            lines.append("Checks:")
            for check in validation["checks"]:
                symbol = "✅" if check["passed"] else "❌"
                lines.append(f"  {symbol} {check['check']}: {check['message']}")
        lines.append("")

        # Errors
        if self.results["errors"]:
            lines.append("⚠️  ERRORS")
            lines.append("-" * 80)
            for error in self.results["errors"]:
                lines.append(f"  • {error}")
            lines.append("")

        lines.append("=" * 80)
        return "\n".join(lines)

    def format_json(self) -> str:
        """Format results as JSON."""
        return json.dumps(self.results, indent=2)

    def format_yaml(self) -> str:
        """Format results as YAML."""
        try:
            import yaml

            return yaml.dump(self.results, default_flow_style=False)
        except ImportError:
            return self.format_json()


def main() -> int:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Test REST API endpoints and validate responses",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python test-api.py https://api.example.com/users
  python test-api.py https://api.example.com/users --method POST --data '{"name":"John"}'
  python test-api.py https://api.example.com/users --auth "your-api-key"
  python test-api.py https://api.example.com/users --output json --verbose
        """,
    )

    parser.add_argument("url", help="API endpoint URL to test")
    parser.add_argument(
        "--method",
        default="GET",
        help="HTTP method (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS)",
    )
    parser.add_argument("--data", help="Request body as JSON string")
    parser.add_argument("--headers", help="Additional headers as JSON string")
    parser.add_argument("--auth", help="Bearer token or API key for authentication")
    parser.add_argument("--timeout", type=int, default=10, help="Request timeout in seconds")
    parser.add_argument(
        "--output", choices=["text", "json", "yaml"], default="text", help="Output format"
    )
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")

    args = parser.parse_args()

    # Create tester
    tester = APITester(args.url, args.method, args.timeout, args.verbose)

    # Parse optional arguments
    data = None
    if args.data:
        data = tester.parse_json_string(args.data)
        if data is None and args.data:
            return 1

    headers = None
    if args.headers:
        headers = tester.parse_json_string(args.headers)
        if headers is None and args.headers:
            return 1

    # Run test
    results = tester.test(data=data, headers=headers, auth_token=args.auth)

    # Format and print results
    if args.output == "json":
        print(tester.format_json())
    elif args.output == "yaml":
        print(tester.format_yaml())
    else:
        print(tester.format_text())

    # Return success if no errors and 2xx status
    if results["errors"]:
        return 1
    if (
        results["response"].get("status_code")
        and not (200 <= results["response"]["status_code"] < 300)
    ):
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
