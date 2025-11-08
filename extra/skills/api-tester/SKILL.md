---
name: api-tester
description: Test REST APIs and generate documentation
---

# API Testing Skill

Comprehensive REST API testing and validation skill that helps test endpoints, validate responses, and generate OpenAPI documentation.

## When to Use

Invoke this skill when:

- ✅ **Testing REST API endpoints** - Make requests to APIs and verify responses
- ✅ **Validating API responses** - Check response structure, status codes, headers
- ✅ **Debugging API issues** - Test different request formats and payloads
- ✅ **Generating API documentation** - Create OpenAPI/Swagger specifications
- ✅ **Verifying API contracts** - Ensure API behavior matches expectations
- ✅ **Load testing** - Test API performance under various conditions
- ✅ **Authentication testing** - Validate API key, token, and authorization
- ✅ **Data validation** - Check request/response data types and formats

## Core Capabilities

### 1. REST API Testing
- **HTTP Methods**: GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS
- **Request Construction**: Build requests with headers, body, parameters, authentication
- **Response Analysis**: Parse JSON, XML, plain text responses
- **Status Code Validation**: Check HTTP status codes and error handling
- **Header Inspection**: Validate response headers and metadata

### 2. Request Building
- **Query Parameters**: `?param1=value&param2=value`
- **Request Bodies**: JSON, form data, XML, plain text
- **Headers**: Content-Type, Authorization, custom headers
- **Authentication**: Bearer tokens, API keys, Basic auth, OAuth
- **Cookies**: Session cookies and custom cookies

### 3. Response Validation
- **Status Codes**: 2xx (success), 4xx (client errors), 5xx (server errors)
- **JSON Schema**: Validate response structure against schema
- **Content Type**: Verify response content type matches expectation
- **Data Types**: Check field types (string, number, boolean, array, object)
- **Required Fields**: Ensure all required fields present
- **Field Formats**: Email, URL, UUID, date validation

### 4. Documentation Generation
- **OpenAPI Specification**: Generate OpenAPI 3.0/3.1 specs
- **Request/Response Examples**: Document example payloads
- **Error Documentation**: Document error responses and codes
- **Authentication Schemes**: Document auth methods used
- **Endpoint Listing**: Create endpoint reference documentation

## Instructions

### Step 1: Parse API Information
Identify and extract:
- **Base URL**: Protocol, domain, port (e.g., `https://api.example.com`)
- **Endpoint Path**: Resource path (e.g., `/api/v1/users`)
- **HTTP Method**: GET, POST, PUT, PATCH, DELETE, etc.
- **Authentication**: Required auth type and credentials
- **Request Format**: JSON, form data, query params, etc.
- **Expected Response**: Content type and structure

### Step 2: Construct HTTP Request
Build the complete request:
```
METHOD /path?params HTTP/1.1
Host: api.example.com
Headers:
  Content-Type: application/json
  Authorization: Bearer token
  [Custom headers]

Request Body:
{
  "field": "value",
  ...
}
```

### Step 3: Make the Request
Execute request using appropriate method:
- **curl**: For command-line testing
- **Node.js fetch**: For JavaScript environments
- **Python requests**: For Python environments
- **Postman collection**: For API documentation
- **REST Client**: For VS Code extension

### Step 4: Analyze Response
Parse and validate response:
- ✅ Extract status code
- ✅ Parse response body
- ✅ Check response headers
- ✅ Validate data structure
- ✅ Verify expected fields
- ✅ Check data types

### Step 5: Generate Documentation
Create comprehensive documentation:
- **OpenAPI Specification**: Machine-readable API spec
- **Example Requests**: cURL and code examples
- **Example Responses**: Complete response samples
- **Error Codes**: Document possible errors
- **Authentication**: Document auth methods
- **Rate Limiting**: Document rate limits if any

## Examples

### Example 1: Test GET Endpoint

**Request**:
```bash
curl -X GET "https://api.example.com/api/v1/users/123" \
  -H "Authorization: Bearer sk_test_abc123" \
  -H "Accept: application/json"
```

**Response**:
```json
{
  "id": "123",
  "name": "John Doe",
  "email": "john@example.com",
  "created_at": "2024-01-15T10:30:00Z"
}
```

**Validation**:
- ✅ Status: 200 OK
- ✅ Content-Type: application/json
- ✅ All required fields present
- ✅ Email format valid
- ✅ Date format ISO 8601

---

### Example 2: Test POST Endpoint with JSON

**Request**:
```bash
curl -X POST "https://api.example.com/api/v1/users" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk_test_abc123" \
  -d '{
    "name": "Jane Smith",
    "email": "jane@example.com",
    "role": "admin"
  }'
```

**Response**:
```json
{
  "id": "456",
  "name": "Jane Smith",
  "email": "jane@example.com",
  "role": "admin",
  "created_at": "2024-11-08T14:25:00Z"
}
```

**Validation**:
- ✅ Status: 201 Created
- ✅ Location header present
- ✅ Response contains created resource
- ✅ All posted fields returned
- ✅ ID auto-generated

---

### Example 3: Test Error Handling

**Request** (invalid data):
```bash
curl -X POST "https://api.example.com/api/v1/users" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk_test_abc123" \
  -d '{"name": ""}'
```

**Response**:
```json
{
  "error": "Validation Error",
  "message": "Validation failed",
  "errors": [
    {
      "field": "name",
      "message": "Name is required and must be non-empty"
    },
    {
      "field": "email",
      "message": "Email is required"
    }
  ]
}
```

**Validation**:
- ✅ Status: 400 Bad Request
- ✅ Error details provided
- ✅ All validation errors listed
- ✅ Helpful error messages

---

### Example 4: Generate OpenAPI Documentation

**Generated Specification**:
```yaml
openapi: 3.0.0
info:
  title: User Management API
  version: 1.0.0
  description: API for managing user accounts

servers:
  - url: https://api.example.com/api/v1

paths:
  /users:
    get:
      summary: List all users
      parameters:
        - name: page
          in: query
          schema:
            type: integer
      responses:
        '200':
          description: List of users
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/User'
    post:
      summary: Create new user
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserInput'
      responses:
        '201':
          description: User created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'

  /users/{id}:
    get:
      summary: Get user by ID
      parameters:
        - name: id
          in: path
          required: true
          schema:
            type: string
      responses:
        '200':
          description: User details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
        '404':
          description: User not found

components:
  schemas:
    User:
      type: object
      required:
        - id
        - name
        - email
      properties:
        id:
          type: string
          description: Unique user identifier
        name:
          type: string
          description: User's full name
        email:
          type: string
          format: email
          description: User's email address
        role:
          type: string
          enum: [user, admin, moderator]
          description: User's role
        created_at:
          type: string
          format: date-time
          description: User creation timestamp

    UserInput:
      type: object
      required:
        - name
        - email
      properties:
        name:
          type: string
          minLength: 1
          maxLength: 255
        email:
          type: string
          format: email
        role:
          type: string
          enum: [user, admin, moderator]

  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT

security:
  - bearerAuth: []
```

---

### Example 5: Test Authentication

**Bearer Token Test**:
```bash
# Valid token
curl -X GET "https://api.example.com/api/v1/profile" \
  -H "Authorization: Bearer sk_test_valid_token_123"

# Invalid token
curl -X GET "https://api.example.com/api/v1/profile" \
  -H "Authorization: Bearer sk_test_invalid_token"

# Missing token
curl -X GET "https://api.example.com/api/v1/profile"
```

**Expected Responses**:
- Valid: 200 OK with user data
- Invalid: 401 Unauthorized with error message
- Missing: 401 Unauthorized with "Missing authorization header"

---

### Example 6: Test Pagination

**Request**:
```bash
curl -X GET "https://api.example.com/api/v1/users?page=2&limit=10" \
  -H "Authorization: Bearer sk_test_abc123"
```

**Response**:
```json
{
  "data": [
    { "id": "11", "name": "User 11", ... },
    { "id": "12", "name": "User 12", ... },
    ...
  ],
  "pagination": {
    "page": 2,
    "limit": 10,
    "total": 100,
    "pages": 10
  }
}
```

**Validation**:
- ✅ Correct page returned
- ✅ Correct number of items
- ✅ Pagination metadata correct
- ✅ Links to first, last, next, prev available

## Output Format

The skill generates structured output:

```
📊 API TEST RESULTS
═══════════════════════════════════════════

🔗 Endpoint: POST /api/v1/users
✅ Status: 201 Created

📋 Request:
   Headers:
     - Content-Type: application/json
     - Authorization: Bearer ***
   Body: { "name": "John", "email": "john@example.com" }

📦 Response:
   Headers:
     - Content-Type: application/json
     - Location: /api/v1/users/123
   Body: { "id": "123", "name": "John", ... }

✔️ Validation Results:
   ✅ Status code correct (201)
   ✅ Content-Type correct (application/json)
   ✅ Required fields present
   ✅ Data types valid
   ✅ Response time: 45ms

⚠️ Warnings:
   ⚠️  Missing X-Request-ID header
   ⚠️  Cache-Control not set

📚 Generated OpenAPI Spec:
   [Complete OpenAPI specification]
```

## Test Scenarios

### Happy Path Testing
- Valid requests with correct data
- Expected successful responses
- Proper status codes
- Complete response data

### Error Testing
- Missing required fields
- Invalid data types
- Malformed requests
- Missing authentication
- Expired tokens
- Rate limit exceeded

### Edge Cases
- Empty data
- Very large payloads
- Special characters in data
- Unicode and international characters
- Boundary values

### Performance Testing
- Response times
- Concurrent requests
- Large datasets
- Memory usage
- Connection pooling

## Integration Points

This skill works with:

- **REST APIs**: Any HTTP/REST API
- **Authentication**: Bearer tokens, API keys, OAuth, Basic auth
- **Content Types**: JSON, XML, form data, plain text
- **Frameworks**: Express, FastAPI, Django, Spring Boot, etc.
- **Tools**: curl, Postman, Insomnia, Thunder Client
- **Documentation**: Swagger UI, ReDoc, API Blueprint

## Common Patterns

### Pattern 1: API Contract Testing
```bash
# Test that API returns expected structure
curl -X GET https://api.example.com/users/123
# Validate response matches schema
```

### Pattern 2: Authentication Flow Testing
```bash
# 1. Login to get token
# 2. Use token in authenticated requests
# 3. Verify token expiration
# 4. Test refresh token flow
```

### Pattern 3: CRUD Operations Testing
```bash
# Create: POST /resource
# Read: GET /resource/:id
# Update: PUT/PATCH /resource/:id
# Delete: DELETE /resource/:id
```

### Pattern 4: Error Response Testing
```bash
# Test each error scenario
# Verify error messages are helpful
# Check error codes are documented
```

## Tips and Best Practices

### Do's
- ✅ Test all HTTP methods your API supports
- ✅ Test both success and error paths
- ✅ Validate response structure and types
- ✅ Test edge cases and boundary values
- ✅ Document all endpoints comprehensively
- ✅ Include example requests and responses
- ✅ Test authentication and authorization
- ✅ Verify performance characteristics

### Don'ts
- ❌ Hard-code real API keys in examples
- ❌ Test against production without approval
- ❌ Ignore error response validation
- ❌ Skip authentication testing
- ❌ Use invalid test data
- ❌ Assume requests always succeed
- ❌ Ignore response headers
- ❌ Skip documentation generation

## Security Considerations

- 🔒 **Never commit real API keys** - Use test/mock keys
- 🔒 **Mask sensitive data** - Show `***` for tokens in logs
- 🔒 **Use HTTPS only** - Ensure encrypted connections
- 🔒 **Validate CORS headers** - Check origin restrictions
- 🔒 **Test rate limiting** - Ensure protection against abuse
- 🔒 **Validate SSL certificates** - Don't skip cert validation
- 🔒 **Test input validation** - Ensure SQL injection prevention
- 🔒 **Check authorization** - Ensure proper access control

## Troubleshooting

### Common Issues

**"Connection refused"**
- Verify API is running
- Check correct host and port
- Ensure network connectivity

**"Invalid JSON in response"**
- Check response content type
- Verify response is not HTML error page
- Check API returned successful status code

**"Unauthorized (401)"**
- Verify auth token is valid
- Check token hasn't expired
- Ensure correct authorization header format
- Verify API key is correct

**"Forbidden (403)"**
- Check user has permission for resource
- Verify API key has correct scopes
- Check rate limiting not exceeded

**"Not Found (404)"**
- Verify endpoint path is correct
- Check resource exists
- Verify API version in URL is correct

## Related Skills and Commands

This skill complements:
- `/document <file_path>` - Generate API documentation
- `/refactor <file_path>` - Improve API code
- `/deploy [environment]` - Deploy API changes
- `api-tester` - This skill for API testing
- Future: `load-tester` - Performance testing
- Future: `mock-server` - Create mock APIs

## Version and Updates

- **Version**: 1.0.0
- **Last Updated**: November 2024
- **Status**: Stable
- **Supported APIs**: REST/HTTP APIs (OpenAPI 3.0+)

## Getting Help

If you encounter issues:

1. **Verify API is accessible**: `curl https://api.example.com/health`
2. **Check API documentation**: Review endpoint specs
3. **Test with Postman**: Verify request format
4. **Check authentication**: Validate credentials
5. **Review error response**: Read API error messages
6. **Enable verbose logging**: Add `-v` flag to curl

---

**Ready to test your API!** Provide an endpoint URL and method, and this skill will handle the testing and documentation generation.
