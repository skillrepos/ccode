# API Tester Scripts

Utility scripts for the API Tester skill that provide command-line tools for testing REST API endpoints.

## Available Scripts

### `test-api.py` - Python API Testing Script

A comprehensive Python script for testing REST API endpoints, validating responses, and generating formatted results.

#### Features

- **HTTP Methods**: Support for GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS
- **Request Building**: JSON bodies, query parameters, custom headers, authentication
- **Response Validation**: Status codes, JSON validation, content-type checking, header inspection
- **Multiple Output Formats**: Text, JSON, and YAML output options
- **Error Handling**: Comprehensive error detection and reporting
- **Verbose Mode**: Detailed logging for debugging

#### Requirements

```bash
pip install requests
```

Optional for YAML output:
```bash
pip install pyyaml
```

#### Installation

The script is executable. Make it accessible in your PATH:

```bash
chmod +x test-api.py
./test-api.py https://api.example.com/users
```

Or run with Python directly:

```bash
python3 test-api.py https://api.example.com/users
```

#### Basic Usage

##### Test GET endpoint (default)
```bash
python3 test-api.py https://api.example.com/users
```

##### Test with custom method
```bash
python3 test-api.py https://api.example.com/users --method GET
python3 test-api.py https://api.example.com/users --method POST
python3 test-api.py https://api.example.com/users --method DELETE
```

##### Test with JSON data (POST)
```bash
python3 test-api.py https://api.example.com/users \
  --method POST \
  --data '{"name":"John","email":"john@example.com"}'
```

##### Test with authentication
```bash
python3 test-api.py https://api.example.com/users \
  --auth "your-api-key-or-token"
```

##### Test with custom headers
```bash
python3 test-api.py https://api.example.com/users \
  --headers '{"X-Custom-Header":"value","X-API-Version":"2"}'
```

##### Set custom timeout
```bash
python3 test-api.py https://api.example.com/users --timeout 30
```

##### Different output formats
```bash
# Text output (default)
python3 test-api.py https://api.example.com/users --output text

# JSON output
python3 test-api.py https://api.example.com/users --output json

# YAML output (requires pyyaml)
python3 test-api.py https://api.example.com/users --output yaml
```

##### Verbose mode
```bash
python3 test-api.py https://api.example.com/users --verbose
```

#### Examples

##### Example 1: Simple GET Request
```bash
python3 test-api.py https://jsonplaceholder.typicode.com/users/1
```

Output:
```
================================================================================
API TEST RESULTS - 2025-11-08T19:20:24.657107
================================================================================

📋 REQUEST
--------------------------------------------------------------------------------
Method: GET
URL:    https://jsonplaceholder.typicode.com/users/1

📦 RESPONSE
--------------------------------------------------------------------------------
Status:       200 OK
Content-Type: application/json
Content-Length: 509 bytes
Response Time: 75.52ms
Body:
{
  "id": 1,
  "name": "Leanne Graham",
  "username": "Bret",
  ...
}

✅ VALIDATION
--------------------------------------------------------------------------------
Is Success (2xx):  ✅ Yes
Is JSON:           ✅ Yes
Valid JSON:        ✅ Yes
Has Content:       ✅ Yes

Checks:
  ✅ Valid JSON: Response is valid JSON
  ✅ Status 2xx Success: Status 200 indicates success
  ✅ Content-Type Header: Content-Type: application/json
  ✅ Server Header: Server: cloudflare

================================================================================
```

##### Example 2: POST Request with Data
```bash
python3 test-api.py https://jsonplaceholder.typicode.com/posts \
  --method POST \
  --data '{"title":"Test","body":"Testing API","userId":1}'
```

##### Example 3: JSON Output
```bash
python3 test-api.py https://api.example.com/users --output json
```

Returns structured JSON:
```json
{
  "timestamp": "2025-11-08T19:20:27.656460",
  "url": "https://api.example.com/users",
  "method": "POST",
  "request": {
    "method": "POST",
    "url": "https://api.example.com/users",
    "headers": {...},
    "body": {...}
  },
  "response": {
    "status_code": 201,
    "status_text": "Created",
    "headers": {...},
    "body": {...},
    "content_length": 82,
    "elapsed_time_ms": 45.23
  },
  "validation": {
    "is_success": true,
    "is_json": true,
    "is_valid_json": true,
    "checks": [...]
  },
  "errors": []
}
```

##### Example 4: Verbose Mode
```bash
python3 test-api.py https://api.example.com/users --verbose
```

Outputs detailed logging:
```
[19:20:24] [INFO] Starting API test
[19:20:24] [INFO] Making GET request to https://api.example.com/users
[19:20:24] [INFO] Response status: 200
[19:20:24] [INFO] API test completed successfully
```

##### Example 5: With Authentication
```bash
python3 test-api.py https://api.example.com/protected \
  --auth "your-bearer-token"
```

#### Command Line Arguments

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `url` | string | Required | API endpoint URL to test |
| `--method` | string | GET | HTTP method (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS) |
| `--data` | JSON string | None | Request body as JSON |
| `--headers` | JSON string | None | Additional headers as JSON |
| `--auth` | string | None | Bearer token or API key |
| `--timeout` | int | 10 | Request timeout in seconds |
| `--output` | choice | text | Output format (text, json, yaml) |
| `--verbose` | flag | False | Enable verbose output |
| `--help` | flag | False | Show help message |

#### Return Codes

- `0` - Success (no errors and 2xx status code)
- `1` - Failure (errors occurred or non-2xx status code)

#### Output Structure

The script generates structured output with:

1. **Timestamp**: When the test was run
2. **Request Details**: Method, URL, headers, body
3. **Response Details**: Status, headers, body, timing
4. **Validation Results**: Success indicators and detailed checks
5. **Errors**: Any errors that occurred

#### Validation Checks

The script performs automatic validation:

- ✅ Valid HTTP status codes (2xx, 4xx, 5xx ranges)
- ✅ Valid JSON parsing
- ✅ Content-Type header verification
- ✅ Content-Length header verification
- ✅ Response time measurement
- ✅ Server header inspection
- ✅ Custom validation checks

#### Error Handling

The script handles common errors gracefully:

- **Connection errors**: Shows detailed error messages
- **Timeout errors**: Reports when request exceeds timeout
- **JSON errors**: Reports invalid JSON with error details
- **Invalid arguments**: Validates URL, method, and JSON inputs
- **Network issues**: Provides helpful troubleshooting messages

#### Tips and Best Practices

1. **Test locally first**: Use local test APIs before production
2. **Use verbose mode for debugging**: Add `--verbose` flag
3. **Save results to file**: Pipe output to file `> results.json`
4. **Use JSON output for parsing**: Use `--output json` for integration
5. **Check status codes**: Validate expected status codes
6. **Test error cases**: Test invalid inputs and error scenarios
7. **Verify headers**: Check important response headers
8. **Measure performance**: Monitor response times

#### Integration Examples

##### With other tools
```bash
# Save results to file
python3 test-api.py https://api.example.com/users --output json > results.json

# Parse JSON with jq
python3 test-api.py https://api.example.com/users --output json | jq '.response.status_code'

# Use in bash script
if python3 test-api.py https://api.example.com/users > /dev/null; then
    echo "API is healthy"
else
    echo "API test failed"
fi
```

##### In CI/CD pipelines
```bash
# Test before deployment
python3 test-api.py $API_URL --timeout 30
if [ $? -ne 0 ]; then
    echo "API health check failed"
    exit 1
fi
```

#### Troubleshooting

##### "requests library not found"
```bash
pip install requests
```

##### "Connection refused"
- Verify API is running
- Check correct host and port
- Ensure network connectivity

##### "Invalid JSON in response"
- Check response content type
- Verify endpoint returns JSON
- Check for error HTML responses

##### "Timeout"
- Increase timeout: `--timeout 30`
- Check API performance
- Verify network connectivity

#### Configuration

The script can be configured through:

1. **Command-line arguments**: Immediate control
2. **Environment variables**: Default values for common options
3. **Configuration files**: Future enhancement

#### Environment Variables (Future)

```bash
export API_TESTER_TIMEOUT=30
export API_TESTER_OUTPUT=json
export API_TESTER_AUTH="your-token"
```

#### Extending the Script

The `APITester` class is designed for extension:

```python
from test_api import APITester

# Create custom tester
tester = APITester("https://api.example.com/users", method="GET")

# Run test
results = tester.test()

# Access results
print(results["response"]["status_code"])
print(results["validation"]["is_success"])
```

#### License

Part of the Claude Code API Tester skill.

#### Related

- API Tester Skill: See `../SKILL.md`
- Documentation: See `../SKILL.md` for comprehensive skill documentation
- Commands: See `.claude/commands/` for related commands
