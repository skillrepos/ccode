---
name: code-quality
description: Analyze code for quality, security, performance, complexity, and provide refactoring suggestions
---

# Code Quality Skill

Comprehensive code analysis skill for multi-language linting, security scanning, performance analysis, complexity metrics, and intelligent refactoring suggestions. Ensures high-quality, maintainable, and secure code across your entire codebase.

## When to Use

Invoke this skill when:

- ✅ **Enforcing coding standards** - Apply linting rules and style guides
- ✅ **Security scanning** - Detect vulnerabilities and security issues
- ✅ **Performance analysis** - Identify performance bottlenecks and optimization opportunities
- ✅ **Complexity measurement** - Analyze cyclomatic complexity and maintainability
- ✅ **Getting refactoring suggestions** - Identify code smells and improvement opportunities
- ✅ **Multi-language projects** - Lint and analyze code in any language
- ✅ **Code review preparation** - Generate comprehensive quality reports
- ✅ **Compliance checking** - Verify adherence to standards and best practices

## Core Capabilities

### 1. Multi-Language Linting

**Supported Languages**:
- ✅ **JavaScript/TypeScript** - ESLint rules, TSLint, formatting
- ✅ **Python** - PEP 8, Pylint, Black formatting
- ✅ **Java** - Checkstyle, SpotBugs, PMD rules
- ✅ **C/C++** - Clang-Format, CppCheck
- ✅ **Go** - golint, gofmt, vet
- ✅ **Ruby** - RuboCop, Rails conventions
- ✅ **PHP** - PHP-CS-Fixer, PHPStan
- ✅ **C#/.NET** - Roslyn analyzers, StyleCop
- ✅ **CSS/SCSS/LESS** - Stylelint, properties order
- ✅ **HTML** - HTMLHint, accessibility checks
- ✅ **Markdown** - Markdown linting, consistency
- ✅ **SQL** - Query optimization, best practices
- ✅ **YAML** - YAML linting, schema validation
- ✅ **JSON** - JSON schema validation

**Linting Categories**:
- **Style Issues**: Formatting, naming conventions, spacing
- **Best Practices**: Anti-patterns, code smell detection
- **Error Prevention**: Potential bugs, type issues
- **Documentation**: Missing comments, docstrings
- **Import/Dependency**: Unused imports, circular dependencies
- **Complexity**: Function length, parameter count, nesting

### 2. Security Scanning

**Vulnerability Detection**:
- ✅ **SQL Injection** - Unsafe query construction
- ✅ **Cross-Site Scripting (XSS)** - Unescaped output, DOM manipulation
- ✅ **Cross-Site Request Forgery (CSRF)** - Missing token validation
- ✅ **Authentication Issues** - Weak auth, exposed credentials
- ✅ **Cryptography Flaws** - Weak algorithms, hardcoded secrets
- ✅ **Path Traversal** - Directory traversal vulnerabilities
- ✅ **Command Injection** - Shell command vulnerabilities
- ✅ **Insecure Dependencies** - Outdated/vulnerable packages
- ✅ **Data Exposure** - Sensitive data logging/exposure
- ✅ **Access Control** - Improper authorization checks
- ✅ **Deserialization** - Unsafe deserialization attacks
- ✅ **Hardcoded Secrets** - API keys, passwords, tokens in code

**Security Checks**:
- Detect hardcoded credentials
- Identify weak cryptographic usage
- Flag dangerous function calls
- Check for outdated dependencies
- Analyze permission and access patterns
- Detect information leakage
- Validate input/output handling
- Check for race conditions

### 3. Performance Analysis

**Performance Issues**:
- ✅ **Algorithmic Complexity** - O(n²) and worse algorithms
- ✅ **Memory Leaks** - Unreleased resources
- ✅ **Unnecessary Operations** - Redundant computations
- ✅ **Inefficient Data Structures** - Wrong collection types
- ✅ **Loop Inefficiencies** - Expensive operations in loops
- ✅ **String Operations** - Concatenation in loops, regex compilation
- ✅ **Database Queries** - N+1 queries, missing indexes
- ✅ **Synchronous Operations** - Blocking calls where async needed
- ✅ **Large Object Allocation** - Excessive memory usage
- ✅ **Rendering Performance** - DOM thrashing, layout thrashing
- ✅ **Network Efficiency** - Unnecessary requests, large payloads
- ✅ **Bundle Size** - Large JavaScript/CSS bundles

**Performance Metrics**:
- Time complexity analysis
- Space complexity estimation
- Memory usage patterns
- CPU usage optimization opportunities
- Latency and throughput analysis
- Caching opportunities

### 4. Complexity Metrics

**Complexity Measurements**:
- ✅ **Cyclomatic Complexity** - Number of decision paths
- ✅ **Cognitive Complexity** - Mental burden of understanding code
- ✅ **Nesting Depth** - Maximum nesting levels
- ✅ **Function Length** - Lines per function
- ✅ **Parameter Count** - Function parameters
- ✅ **Class Size** - Lines per class/module
- ✅ **Maintainability Index** - Overall code maintainability
- ✅ **Fan-in/Fan-out** - Dependency coupling

**Thresholds & Standards**:
- Cyclomatic Complexity: ≤ 10 (good), 11-20 (moderate), > 20 (high)
- Cognitive Complexity: ≤ 15 (good), 16-25 (moderate), > 25 (high)
- Function Length: ≤ 50 lines (good), 51-100 (moderate), > 100 (high)
- Parameters: ≤ 4 (good), 5-7 (moderate), > 7 (high)
- Class Size: ≤ 200 lines (good), 201-400 (moderate), > 400 (high)
- Nesting Depth: ≤ 3 (good), 4-5 (moderate), > 5 (high)

### 5. Refactoring Suggestions

**Suggested Refactorings**:
- ✅ **Extract Method** - Break large functions
- ✅ **Extract Variable** - Name complex expressions
- ✅ **Inline Variable** - Remove unnecessary variables
- ✅ **Simplify Logic** - Reduce conditional complexity
- ✅ **Remove Duplication** - DRY principle violations
- ✅ **Improve Naming** - Unclear variable/function names
- ✅ **Early Return** - Reduce nesting
- ✅ **Guard Clauses** - Replace nested if/else
- ✅ **Extract Class** - Separate concerns
- ✅ **Move Method** - Better organization
- ✅ **Introduce Parameter Object** - Simplify parameters
- ✅ **Replace Magic Numbers** - Use named constants

## Instructions

### Step 1: Understand the Code

Examine:
- **Language** - Identify programming language
- **Scope** - Single file, module, or codebase
- **Context** - Purpose and usage patterns
- **Dependencies** - Related modules and libraries
- **Standards** - Team conventions and guidelines

### Step 2: Apply Multi-Language Linting

Check for:
- **Style violations** - Formatting, naming, conventions
- **Best practice violations** - Anti-patterns, code smells
- **Error-prone patterns** - Potential bugs
- **Missing documentation** - Undocumented code
- **Import issues** - Unused/circular dependencies
- **Complexity issues** - Overly complex code

### Step 3: Perform Security Scanning

Analyze for:
- **Injection vulnerabilities** - SQL, command, template injection
- **Authentication flaws** - Weak auth, exposure
- **Cryptographic issues** - Weak algorithms, bad practices
- **Data exposure** - Hardcoded secrets, logging sensitive data
- **Access control** - Missing authorization checks
- **Insecure dependencies** - Vulnerable packages
- **Input validation** - Unvalidated input processing
- **Output encoding** - Unescaped output

### Step 4: Analyze Performance

Identify:
- **Algorithmic inefficiencies** - Poor algorithms
- **Memory issues** - Leaks, excessive allocation
- **Loop inefficiencies** - Expensive operations repeated
- **Database issues** - N+1 queries, bad indexes
- **I/O inefficiencies** - Synchronous when async preferred
- **Caching opportunities** - Recomputed values
- **Bundle size** - Large assets

### Step 5: Calculate Complexity Metrics

Measure:
- **Cyclomatic complexity** - Number of paths
- **Cognitive complexity** - Mental effort
- **Function metrics** - Length, parameters
- **Class metrics** - Size, cohesion
- **Dependency metrics** - Coupling, cohesion
- **Maintainability index** - Overall quality score

### Step 6: Generate Refactoring Plan

Suggest:
- **High-priority** - Critical issues (security, performance)
- **Medium-priority** - Code quality improvements
- **Low-priority** - Style and polish
- **Before/after** - Code examples
- **Benefits** - Why the refactoring matters
- **Implementation** - How to apply the change

## Examples

### Example 1: JavaScript Linting Issues

**Code to Analyze**:
```javascript
function processUsers(users){
var active_users = [];
for(var i = 0; i < users.length; i++){
if(users[i].status=="active"){
active_users.push(users[i]);
}
}
return active_users;
}
```

**Issues Found**:

| Issue | Type | Severity | Message |
|-------|------|----------|---------|
| Missing semicolons | Style | Low | Add semicolons at statement ends |
| snake_case naming | Style | Low | Use camelCase for variable names |
| var instead of const | Best Practice | Medium | Use const/let instead of var |
| Loose equality (==) | Error Prevention | Medium | Use strict equality (===) |
| Can use filter() | Best Practice | Medium | Use array methods instead of loops |
| No docstring | Documentation | Low | Add JSDoc comment |

**Refactored Code**:
```javascript
/**
 * Filter and return active users
 * @param {Array<User>} users - Array of user objects
 * @returns {Array<User>} Active users only
 */
function processUsers(users) {
  return users.filter(user => user.status === 'active');
}
```

**Benefits**:
- 5 lines → 1 line (80% reduction)
- More readable and maintainable
- Follows functional programming patterns
- Better performance (optimized filter)
- Type-safe with JSDoc

---

### Example 2: Security Vulnerabilities

**Code to Analyze** (Python):
```python
import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route('/user/<user_id>')
def get_user(user_id):
    db = sqlite3.connect(':memory:')
    cursor = db.cursor()

    # VULNERABLE: SQL Injection
    query = f"SELECT * FROM users WHERE id = {user_id}"
    result = cursor.execute(query).fetchone()

    return str(result)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # VULNERABLE: Hardcoded credentials, no password hashing
    if username == 'admin' and password == 'admin123':
        return "Login successful"

    return "Login failed"
```

**Security Issues Found**:

| Issue | Type | Severity | OWASP |
|-------|------|----------|-------|
| SQL Injection | Vulnerability | CRITICAL | A03:2021 |
| String interpolation in query | Vulnerability | CRITICAL | A03:2021 |
| Hardcoded credentials | Vulnerability | CRITICAL | A02:2021 |
| Plain text password | Vulnerability | CRITICAL | A02:2021 |
| No authentication check | Vulnerability | HIGH | A07:2021 |
| Exposed error messages | Vulnerability | MEDIUM | A01:2021 |

**Secure Code**:
```python
import sqlite3
import os
from flask import Flask, request
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

@app.route('/user/<user_id>')
def get_user(user_id):
    db = sqlite3.connect(':memory:')
    cursor = db.cursor()

    # SECURE: Parameterized query prevents SQL injection
    query = "SELECT * FROM users WHERE id = ?"
    result = cursor.execute(query, (user_id,)).fetchone()

    if not result:
        return {"error": "User not found"}, 404

    return {"user": result}

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '').strip()
    password = request.form.get('password', '')

    # SECURE: Use proper authentication
    user = get_user_from_db(username)
    if user and check_password_hash(user['password_hash'], password):
        # Set secure session
        return {"message": "Login successful"}

    # Don't reveal which field was wrong
    return {"error": "Invalid credentials"}, 401
```

---

### Example 3: Performance Issues

**Code to Analyze**:
```javascript
// SLOW: O(n²) complexity, string concatenation in loop
function getUsersSummary(users) {
  let summary = '';
  for (let i = 0; i < users.length; i++) {
    summary += 'User: ' + users[i].name + ', Email: ' + users[i].email + '\n';
    // SLOW: Repeated DOM query in loop
    document.getElementById('count').innerText = (i + 1);
  }
  return summary;
}

// SLOW: N+1 queries
function getUsersWithPosts() {
  const users = db.query('SELECT * FROM users');
  users.forEach(user => {
    // This query runs for EACH user - N+1 problem!
    user.posts = db.query('SELECT * FROM posts WHERE user_id = ?', [user.id]);
  });
  return users;
}
```

**Performance Issues**:

| Issue | Type | Impact | Severity |
|-------|------|--------|----------|
| String concatenation in loop | Performance | O(n²) complexity | HIGH |
| DOM manipulation in loop | Performance | Reflow/repaint per iteration | HIGH |
| N+1 query pattern | Database | 1 + N queries instead of 1-2 | CRITICAL |
| No pagination | Performance | All data loaded at once | HIGH |

**Optimized Code**:
```javascript
// FAST: O(n) complexity, efficient string building
function getUsersSummary(users) {
  // Use array join instead of concatenation
  const lines = users.map(user =>
    `User: ${user.name}, Email: ${user.email}`
  );

  // Update DOM once, not in loop
  document.getElementById('count').innerText = users.length;

  return lines.join('\n');
}

// FAST: Single query with JOIN
function getUsersWithPosts() {
  // Use JOIN to get all data in one query
  return db.query(`
    SELECT u.*, p.id as post_id, p.title
    FROM users u
    LEFT JOIN posts p ON u.id = p.user_id
    ORDER BY u.id
  `);
}
```

**Performance Improvements**:
- String building: O(n) instead of O(n²)
- DOM updates: 1 instead of n
- Database queries: 1-2 instead of 1+n
- Memory: Reduced allocations

---

### Example 4: Complexity Metrics Report

**Code Analyzed**:
```python
def process_payment(amount, user_type, card, address):
    """Process a payment with multiple conditions."""
    if user_type == 'premium':
        if amount > 10000:
            if card.is_verified:
                if address.is_verified:
                    charge_amount = amount * 0.9  # 10% discount
                    if card.balance >= charge_amount:
                        process_charge(charge_amount)
                    else:
                        raise Exception("Insufficient funds")
                else:
                    raise Exception("Address not verified")
            else:
                raise Exception("Card not verified")
        else:
            charge_amount = amount
            process_charge(charge_amount)
    else:
        if amount > 5000:
            if card.is_verified:
                charge_amount = amount * 1.05  # 5% fee
                process_charge(charge_amount)
        else:
            process_charge(amount)
```

**Metrics Report**:

```
COMPLEXITY ANALYSIS
═══════════════════════════════════════════════════════════

Cyclomatic Complexity: 11 (HIGH ⚠️)
  - Target: ≤ 10
  - Status: Exceeds recommended threshold
  - Risk: Difficult to test, error-prone

Cognitive Complexity: 18 (HIGH ⚠️)
  - Target: ≤ 15
  - Status: Exceeds recommended threshold
  - Risk: Hard to understand and maintain

Function Metrics:
  - Lines of Code: 22 (HIGH)
  - Parameters: 4 (GOOD)
  - Nesting Depth: 5 (HIGH ⚠️)
  - Branches: 11 (HIGH)

Maintainability Index: 62/100 (MODERATE)
  - Scale: 0-100 (higher is better)
  - Status: Below ideal (target: 70+)
  - Risk: Medium maintenance difficulty

TEST COVERAGE NEEDS:
  - Paths to cover: 11
  - Estimated cases: 20+
  - Recommendation: High test coverage required
```

**Refactored Code** (Reduced complexity):
```python
def process_payment(amount, user_type, card, address):
    """Process a payment with validation and discount logic."""

    # Early validation
    validate_payment(amount, user_type, card, address)

    # Calculate charge with discount rules
    charge_amount = calculate_charge(amount, user_type)

    # Process charge
    process_charge(charge_amount)

def validate_payment(amount, user_type, card, address):
    """Validate payment prerequisites."""
    if not card.is_verified:
        raise Exception("Card not verified")

    if user_type == 'premium' and amount > 10000:
        if not address.is_verified:
            raise Exception("Address not verified")

    if card.balance < amount:
        raise Exception("Insufficient funds")

def calculate_charge(amount, user_type):
    """Calculate final charge with discounts/fees."""
    if user_type == 'premium' and amount > 10000:
        return amount * 0.9  # 10% discount

    if amount > 5000:
        return amount * 1.05  # 5% fee

    return amount
```

**Improvement Results**:
- Cyclomatic Complexity: 11 → 5 (55% reduction)
- Cognitive Complexity: 18 → 8 (56% reduction)
- Function Length: 22 → 3 lines (main function)
- Nesting Depth: 5 → 2 (60% reduction)
- Testability: Much improved
- Readability: Significantly better

---

### Example 5: Multi-Language Analysis

**Project Files**:
- `auth.js` (JavaScript)
- `database.py` (Python)
- `api.go` (Go)
- `queries.sql` (SQL)

**Analysis Report**:

```
MULTI-LANGUAGE CODE QUALITY REPORT
═══════════════════════════════════════════════════════

JavaScript (auth.js)
──────────────────────────────────────────────────────
Issues: 8
  ⚠️  [6] Style violations
  ⚠️  [1] Best practice violation
  🔴 [1] Security issue (XSS vulnerability)

Suggestions:
  → Use const/let instead of var (2 occurrences)
  → Add input sanitization for DOM operations
  → Extract method: authentication logic too long

Python (database.py)
──────────────────────────────────────────────────────
Issues: 5
  ⚠️  [3] PEP 8 style violations
  ⚠️  [1] Missing docstring
  🔴 [1] Security issue (hardcoded connection string)

Suggestions:
  → Add type hints for better code clarity
  → Move credentials to environment variables
  → Add connection pooling for performance

Go (api.go)
──────────────────────────────────────────────────────
Issues: 3
  ⚠️  [2] Error handling could be improved
  ⚠️  [1] Unused import

Suggestions:
  → Add logging for debugging
  → Implement proper error wrapping
  → Consider middleware for error handling

SQL (queries.sql)
──────────────────────────────────────────────────────
Issues: 4
  ⚠️  [2] Missing indexes on foreign keys
  ⚠️  [1] Inefficient JOIN query
  ⚠️  [1] No pagination limit

Suggestions:
  → Add index: CREATE INDEX idx_user_id ON posts(user_id)
  → Rewrite JOIN to avoid full table scans
  → Add LIMIT clause for large result sets

═══════════════════════════════════════════════════════

OVERALL QUALITY SCORE: 72/100 (GOOD)
  - Code Quality: 75/100
  - Security: 65/100 ⚠️
  - Performance: 70/100
  - Complexity: 78/100
  - Best Practices: 72/100

PRIORITY ACTIONS:
  1. 🔴 CRITICAL: Fix SQL injection vulnerability in auth.js
  2. 🔴 CRITICAL: Move database credentials to environment
  3. 🟡 HIGH: Add missing SQL indexes
  4. 🟡 HIGH: Improve error handling in Go code
  5. 🟢 MEDIUM: Code style and formatting fixes
```

## Best Practices by Language

### JavaScript/TypeScript
- ✅ Use const/let, avoid var
- ✅ Use strict equality (===)
- ✅ Add JSDoc comments
- ✅ Avoid callback hell (use async/await)
- ✅ Use array methods over loops
- ✅ Proper error handling

### Python
- ✅ Follow PEP 8 style guide
- ✅ Use type hints
- ✅ Proper exception handling
- ✅ Document with docstrings
- ✅ Use context managers for resources
- ✅ Avoid mutable default arguments

### Java
- ✅ Follow naming conventions
- ✅ Proper exception handling
- ✅ Use generics for type safety
- ✅ Implement equals/hashCode properly
- ✅ Immutable objects where possible
- ✅ Proper resource management

### Go
- ✅ Handle errors explicitly
- ✅ Use defer for cleanup
- ✅ Follow standard library conventions
- ✅ Use interfaces for flexibility
- ✅ Proper concurrency patterns
- ✅ Write benchmarks for hot paths

### C/C++
- ✅ Use modern C++ (C++17+)
- ✅ Smart pointers for memory
- ✅ Const correctness
- ✅ RAII pattern
- ✅ Avoid manual memory management
- ✅ Use STL containers

## Security Checklist

### Authentication & Authorization
- ✅ Secure password hashing (bcrypt, argon2)
- ✅ Secure session management
- ✅ Proper authorization checks
- ✅ Multi-factor authentication support
- ✅ Secure logout/session invalidation
- ✅ Account lockout after failed attempts

### Data Protection
- ✅ Encrypt sensitive data at rest
- ✅ Use HTTPS for data in transit
- ✅ Proper input validation
- ✅ Output encoding/escaping
- ✅ No hardcoded secrets
- ✅ Secure logging practices

### Vulnerability Prevention
- ✅ SQL injection prevention (parameterized queries)
- ✅ XSS prevention (output encoding)
- ✅ CSRF protection (tokens)
- ✅ Command injection prevention
- ✅ Path traversal prevention
- ✅ Dependency vulnerability scanning

## Performance Optimization Checklist

### Algorithmic
- ✅ Choose correct data structures
- ✅ Use appropriate algorithms
- ✅ Avoid O(n²) in loops
- ✅ Memoization for repeated calculations
- ✅ Lazy evaluation where appropriate

### Memory
- ✅ Avoid memory leaks
- ✅ Proper resource cleanup
- ✅ Efficient data structures
- ✅ Avoid excessive allocations
- ✅ Use object pooling when needed

### I/O
- ✅ Batch operations
- ✅ Use async where appropriate
- ✅ Proper connection pooling
- ✅ Caching strategy
- ✅ Pagination for large datasets

## Output Format

Analysis generates structured output with:

```
📊 CODE QUALITY ANALYSIS REPORT
═══════════════════════════════════════════════════════

FILE: src/auth.js

🔍 LINTING ISSUES (8 issues found)
  Category | Count | Severity | Examples
  ─────────┼───────┼──────────┼──────────
  Style    | 6     | Low      | Missing semicolons, spacing
  Best Practice | 1 | Medium | Use const instead of var
  Security | 1     | Critical | XSS vulnerability

🔐 SECURITY SCAN (3 vulnerabilities)
  [CRITICAL] XSS: Unescaped DOM write at line 45
  [HIGH] Missing input validation at line 23
  [MEDIUM] Weak password validation at line 18

⚡ PERFORMANCE ISSUES (2 issues)
  [HIGH] String concatenation in loop (line 32)
  [MEDIUM] Unnecessary array copy (line 56)

📈 COMPLEXITY METRICS
  Cyclomatic: 12 (HIGH)
  Cognitive: 16 (HIGH)
  Function Length: 45 lines
  Maintainability Index: 68/100

💡 REFACTORING SUGGESTIONS
  1. Extract authentication logic to separate function
  2. Add input sanitization helper
  3. Use template literals instead of concatenation
  4. Break long function into smaller units

✅ SUMMARY
  Total Issues: 13
  Security Risk: 🔴 HIGH
  Code Quality: 🟡 MEDIUM
  Overall Score: 65/100
```

## Integration Examples

### With /refactor Command
```
/refactor src/auth.js
→ Uses code-quality skill to analyze
→ Generates refactoring suggestions
→ Applies improvements
```

### With /deploy Command
```
/deploy production
→ Runs code-quality scan as pre-check
→ Fails deployment if critical issues found
→ Reports quality metrics
```

### In Development Workflow
```
1. Write code
2. Use code-quality skill: "Analyze this code"
3. Fix issues reported
4. /commit "fix: improve code quality"
```

## Supported Analysis Tools

The skill leverages or references:
- ESLint, TypeScript, Prettier (JavaScript)
- Pylint, Black, Bandit (Python)
- Checkstyle, PMD, SpotBugs (Java)
- golint, gofmt, go vet (Go)
- Clang, CppCheck (C/C++)
- RuboCop (Ruby)
- PHP-CS-Fixer, PHPStan (PHP)
- SQLFluff (SQL)
- StyleLint (CSS)
- And language-specific linters

## Metrics Interpretation

### Cyclomatic Complexity
- **1-5**: Simple, low risk ✅
- **6-10**: Moderate, manageable ⚠️
- **11-15**: Complex, high risk 🔴
- **16+**: Very complex, refactor 🔴

### Cognitive Complexity
- **1-5**: Easy to understand ✅
- **6-15**: Moderate effort ⚠️
- **16-25**: High effort 🔴
- **26+**: Very difficult 🔴

### Maintainability Index
- **71-100**: Highly maintainable ✅
- **56-70**: Maintainable ⚠️
- **40-55**: Low maintainability 🔴
- **0-39**: Not maintainable 🔴

## Version History

- **v2.0** - Added multi-language support
- **v1.5** - Enhanced security scanning
- **v1.0** - Initial release

## Getting Help

When requesting code quality analysis, provide:

1. **Code sample** - File or code snippet
2. **Language** - Programming language
3. **Context** - Purpose and environment
4. **Concerns** - What aspects to focus on
5. **Standards** - Team guidelines to follow

Example request:
```
"Analyze this Python database code for security issues
and suggest optimizations. We follow PEP 8 and have a
maximum cyclomatic complexity of 10."
```

---

**Skill Status**: Production-ready
**Last Updated**: November 2024
**Integration**: Works with /refactor, /deploy, /test commands
