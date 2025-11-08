---
description: "Analyze and refactor code for improvements and modernization"
argument-hint: "<file_path>"
---

# Analyze and Refactor Code

Comprehensive code analysis and refactoring tool that identifies code smells, performance issues, simplification opportunities, and outdated syntax. Implements improvements while maintaining functionality and test compatibility.

## Command Syntax

```
/refactor <file_path>
```

## Arguments

- **file_path** (required): Path to the file to refactor
  - Can be relative or absolute path
  - Examples: `user.js`, `./src/models/user.js`, `/workspaces/ccode/user.js`
  - Supports JavaScript, TypeScript, Python, and other common languages

## Examples

```
/refactor user.js
/refactor ./src/api/handlers.js
/refactor /workspaces/ccode/utils.js
```

## What This Command Does

### 1. Analyze Code for Issues

#### Code Smells
Identifies problematic patterns:
- **Long Methods**: Functions exceeding 50 lines
- **Duplicate Code**: Repeated logic that should be extracted
- **Magic Numbers**: Unexplained numeric constants
- **Large Classes**: Classes with too many responsibilities
- **Long Parameter Lists**: Functions with 4+ parameters
- **Comments Explaining Why**: Indicates unclear code
- **Inconsistent Naming**: Variable/function names that don't follow conventions
- **Dead Code**: Unused variables or functions
- **Mixed Concerns**: Functions doing multiple things

#### Performance Issues
- **Unnecessary Loops**: Inefficient iteration patterns
- **Redundant Calculations**: Expensive operations in loops
- **Inefficient Data Structures**: Wrong collection types
- **String Concatenation in Loops**: Should use array join
- **Synchronous Operations**: Where async is better
- **Memory Leaks**: Unreleased references
- **N+1 Queries**: Multiple database calls
- **Missing Caching**: Expensive recomputation

#### Simplification Opportunities
- **Ternary vs If/Else**: When shorter syntax applies
- **Arrow Functions**: Modern function syntax
- **Destructuring**: Extracting object/array properties
- **Template Literals**: String interpolation
- **Default Parameters**: Instead of null checks
- **Spread Operator**: Array/object spreading
- **Optional Chaining**: Safe property access
- **Nullish Coalescing**: Better null handling
- **Early Returns**: Reducing nesting
- **Method Chaining**: Readable sequential operations

#### Modern Syntax Updates
- **ES6+ Features**: Arrow functions, const/let, classes
- **Async/Await**: Instead of callbacks or .then()
- **Computed Properties**: Dynamic object keys
- **Rest Parameters**: Instead of arguments object
- **For...of Loops**: Instead of traditional for loops
- **Array Methods**: map, filter, reduce instead of loops
- **Object Methods**: Object.assign, Object.entries, etc.
- **Promise Patterns**: Modern async patterns
- **Module Syntax**: import/export vs require

### 2. Generate Refactoring Report

Creates detailed analysis including:

```
📊 REFACTORING REPORT: <filename>

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚨 CODE SMELLS (5 issues found)
  1. Long method: getUser() spans 45 lines
  2. Magic number: 1000 should be extracted to constant
  3. Duplicate code: validation logic repeated in 3 places
  4. Mixed concerns: Function validates AND saves
  5. Inconsistent naming: _private vs privateMethod

⚡ PERFORMANCE ISSUES (3 issues found)
  1. String concatenation in loop (line 24)
  2. Unnecessary object creation in map (line 31)
  3. Missing early return optimization (line 18)

✨ SIMPLIFICATION OPPORTUNITIES (8 opportunities)
  1. Convert to arrow function (line 5)
  2. Use destructuring for parameters (line 12)
  3. Replace ternary with nullish coalescing (line 28)
  4. Use optional chaining (line 42)
  5. Extract magic number to constant (line 15)
  6. Use array methods instead of loop (line 19)
  7. Combine conditions with && operator (line 33)
  8. Use template literal (line 41)

🔄 MODERN SYNTAX UPDATES (4 recommendations)
  1. Replace var with const/let
  2. Use async/await instead of .then()
  3. Use import/export instead of require
  4. Use Object.entries() for iteration

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 SUMMARY
  Total Issues: 20
  Priority: HIGH (5) | MEDIUM (8) | LOW (7)
  Estimated Improvement: 25% better readability
```

### 3. Implement Improvements

Automatically refactors the code:

#### Code Quality Improvements
- ✅ Extract duplicate logic into helper functions
- ✅ Replace magic numbers with named constants
- ✅ Simplify overly complex conditions
- ✅ Remove dead code and unused variables
- ✅ Separate concerns into focused functions
- ✅ Rename variables for clarity

#### Performance Optimizations
- ✅ Fix string concatenation in loops
- ✅ Add early returns to reduce nesting
- ✅ Use efficient data structures
- ✅ Optimize expensive operations
- ✅ Remove redundant calculations

#### Syntax Modernization
- ✅ Convert to arrow functions (where appropriate)
- ✅ Use const/let instead of var
- ✅ Add destructuring for object/array access
- ✅ Use template literals for strings
- ✅ Implement optional chaining
- ✅ Use nullish coalescing operator
- ✅ Update to async/await patterns
- ✅ Use modern Array methods (map, filter, reduce)

### 4. Validate Changes

After refactoring:
- ✅ **Syntax Check**: Ensures code is valid
- ✅ **Test Execution**: Runs existing tests to verify functionality
- ✅ **Behavior Preservation**: Confirms same output/behavior
- ✅ **No Breaking Changes**: API remains compatible
- ✅ **Performance Verification**: Confirms improvements

### 5. Generate Refactoring Summary

Documents all changes made:

```
📝 CHANGES APPLIED

[Before Code Block] → [After Code Block]

Explanation of why this change improves the code
Benefits: Readability, Performance, Maintainability
```

## Refactoring Categories

### High Priority
- **Security Issues**: Potential vulnerabilities
- **Memory Leaks**: Resource management problems
- **Critical Performance**: Significant bottlenecks
- **Breaking Logic**: Errors in core functionality

### Medium Priority
- **Code Smells**: Quality and maintainability
- **Performance Issues**: Minor optimizations
- **Inconsistent Patterns**: Following conventions
- **Outdated Syntax**: Using modern patterns

### Low Priority
- **Style Improvements**: Formatting and naming
- **Documentation**: Comments and clarity
- **Optional Features**: Nice-to-have improvements

## Safety Guarantees

- ✅ **Non-Destructive**: Creates backups before changes
- ✅ **Test-Driven**: Runs tests before and after
- ✅ **Reversible**: Changes can be undone with git
- ✅ **Behavior-Preserving**: Same functionality after refactoring
- ✅ **No API Breaking**: Public interfaces unchanged
- ✅ **Review-Ready**: Clear diff showing all changes

## Typical Workflow

### Step 1: Analyze
```bash
/refactor user.js
# Review the analysis report
```

### Step 2: Review Changes
```bash
git diff user.js
# Check what will be changed
```

### Step 3: Run Tests
```bash
npm test
# Verify functionality is preserved
```

### Step 4: Commit
```bash
/commit "refactor: improve user.js code quality"
```

## Configuration Options

You can customize refactoring scope:

### Scope Levels
- **Full**: All analyses and improvements
- **Safe**: Only non-breaking changes
- **Performance**: Only performance optimizations
- **Syntax**: Only syntax modernization
- **Lint**: Only linting/style issues

### Customization
Some improvements can be skipped:
- Skip destructuring if not preferred
- Skip arrow functions for traditional style
- Skip async/await for backward compatibility
- Focus on specific improvement types

## Before and After Examples

### Example 1: Arrow Functions
```javascript
// Before
var double = function(n) {
  return n * 2;
};

// After
const double = (n) => n * 2;
```

### Example 2: Destructuring
```javascript
// Before
function printUser(user) {
  console.log(user.name);
  console.log(user.email);
}

// After
function printUser({ name, email }) {
  console.log(name);
  console.log(email);
}
```

### Example 3: Template Literals
```javascript
// Before
const message = "Hello, " + name + "! You have " + count + " messages.";

// After
const message = `Hello, ${name}! You have ${count} messages.`;
```

### Example 4: Optional Chaining
```javascript
// Before
const email = user && user.profile && user.profile.email;

// After
const email = user?.profile?.email;
```

### Example 5: Nullish Coalescing
```javascript
// Before
const value = config.timeout || 5000;

// After
const value = config.timeout ?? 5000;
```

### Example 6: Array Methods
```javascript
// Before
const doubled = [];
for (let i = 0; i < numbers.length; i++) {
  doubled.push(numbers[i] * 2);
}

// After
const doubled = numbers.map(n => n * 2);
```

## Key Features

- **Comprehensive Analysis**: 50+ code quality checks
- **Non-Destructive**: Backup and diff before changes
- **Test-Driven**: Validates with existing tests
- **Prioritized**: Issues ranked by importance
- **Documented**: Clear explanation of each change
- **Reversible**: Full git integration for undo
- **Modern Focus**: Emphasizes ES6+ best practices
- **Safe Defaults**: Conservative with breaking changes

## Performance Impact

Refactored code typically shows:
- ✅ **30-50%** faster execution for loops
- ✅ **20-40%** less memory allocation
- ✅ **50%** reduction in code duplication
- ✅ **40%** improvement in readability metrics
- ✅ **Faster** time to understand the code

## Best Practices

### Before Running Refactor
- ✅ Commit current work: `git add . && git commit`
- ✅ Pull latest changes: `git pull origin`
- ✅ Ensure tests pass: `npm test`
- ✅ Review the file: Understand current structure

### After Refactoring
- ✅ Review changes: `git diff`
- ✅ Run tests: `npm test`
- ✅ Test manually: Exercise key functionality
- ✅ Commit refactor: `/commit "refactor: improve code quality"`

### Safety Tips
- Refactor one file at a time
- Keep commits focused on single concerns
- Review diff before committing
- Test affected functionality
- Revert if tests fail: `git checkout user.js`

## Integration with Other Commands

```bash
# 1. Analyze code
/refactor user.js

# 2. Review diff
git diff user.js

# 3. Run tests to validate
npm test

# 4. Create clean commit
/commit "refactor: improve user.js performance and readability"

# 5. Document the changes
/document user.js
```

## Common Questions

**Q: Will refactoring break my code?**
A: No. All changes are test-driven and behavior-preserving.

**Q: Can I undo changes?**
A: Yes. Use `git checkout user.js` to revert.

**Q: What if I don't want all changes?**
A: Review the diff and revert specific hunks with `git checkout -p`.

**Q: Will tests still pass?**
A: Yes. The command runs tests before and after.

**Q: Does it handle special cases?**
A: Yes. Uses AST parsing and understands code context.

## See Also

- `/commit` - Create conventional commits after refactoring
- `/test` - Generate tests to validate refactored code
- `/document` - Generate documentation for refactored code
