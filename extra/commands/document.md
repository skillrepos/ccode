---
description: "Generate comprehensive documentation for a file or module"
argument-hint: "<file_path>"
---

# Generate Comprehensive Documentation

Analyzes a file and creates complete documentation including JSDoc/docstring comments, README sections, usage examples, and API documentation.

## Command Syntax

```
/document <file_path>
```

## Arguments

- **file_path** (required): Path to the file to document
  - Can be relative or absolute path
  - Examples: `user.js`, `./src/models/user.js`, `/workspaces/ccode/user.js`
  - Supports JavaScript, TypeScript, Python, and other common languages

## Examples

```
/document user.js
/document ./src/api/handlers.js
/document /workspaces/ccode/user.js
```

## What This Command Does

### 1. Analyze the File Structure
- Parses the file to identify:
  - Classes and their methods
  - Functions and their parameters
  - Exported modules and APIs
  - Dependencies and imports
  - Purpose and functionality

### 2. Generate JSDoc/Docstring Comments
- Creates comprehensive JSDoc comments for:
  - **Classes**: Purpose, constructor parameters, properties
  - **Methods**: Description, parameters with types, return values, throws errors
  - **Functions**: Purpose, parameter types, return types, examples
  - **Properties**: Type information, description, default values
- Follows JSDoc/documentation best practices
- Includes `@param`, `@returns`, `@throws`, `@example` tags
- Ensures all public APIs are documented

### 3. Create README Section
- Generates documentation section including:
  - **Module Overview**: What the module does
  - **Purpose**: Why it exists and when to use it
  - **Key Features**: Main capabilities at a glance
  - **Dependencies**: Required modules and libraries
  - **Architecture Notes**: Design patterns and decisions

### 4. Provide Usage Examples
- Creates practical code examples showing:
  - How to import/require the module
  - Basic usage patterns
  - Common workflows
  - Error handling examples
  - Edge cases and special scenarios
- Examples are copy-paste ready and runnable

### 5. Generate API Documentation
- For classes and exported functions:
  - Parameter specifications with types
  - Return value specifications
  - Error/exception documentation
  - Detailed method signatures
  - Property definitions
- Creates reference-style documentation
- Includes type information where applicable

## Output Organization

The command generates documentation in the following structure:

```
📄 File: <filename>

## 1. JSDoc Comments
[Complete JSDoc annotations for the file]

## 2. Module Documentation
### Overview
[What the module does]

### Key Features
- Feature 1
- Feature 2

### Dependencies
- Dependency list

## 3. Usage Examples
### Basic Usage
[Example code]

### Advanced Usage
[More complex examples]

### Error Handling
[Exception handling examples]

## 4. API Reference
### Classes
- ClassName
  - constructor()
  - method1()
  - method2()

### Functions
- functionName()

### Properties
- propertyName: type
```

## Features

- **Automatic JSDoc Generation**: Creates properly formatted documentation comments
- **Type Inference**: Detects and documents parameter and return types
- **Example Generation**: Provides practical, working code examples
- **API Reference**: Complete method and function documentation
- **README Integration**: Sections ready to copy into project documentation
- **Multi-Language Support**: Works with JavaScript, TypeScript, Python, and more
- **Standards Compliant**: Follows JSDoc, Google, and industry documentation standards

## Documentation Standards

### JSDoc Format
```javascript
/**
 * Description of what this does
 * @param {string} name - Parameter description
 * @param {number} [optional=default] - Optional parameter
 * @returns {Object} Description of return value
 * @throws {Error} When this error occurs
 * @example
 * const result = myFunction('value');
 */
```

### Type Annotations Included
- Parameter types: `{string}`, `{number}`, `{Array}`, `{Object}`, etc.
- Optional parameters: `[paramName]` notation
- Default values: `[paramName=default]` notation
- Union types: `{string|number}`
- Complex types: `{Object.<string, number>}`

### Examples Include
- Basic usage
- Common workflows
- Error scenarios
- Edge cases
- Integration patterns

## Integration with Your Project

After running `/document`:

1. **Copy JSDoc Comments**: Add them to your source file for IDE autocomplete
2. **Update README.md**: Integrate the generated API documentation section
3. **Share with Team**: Use examples and API reference in documentation
4. **Keep Current**: Re-run when significant changes are made to keep docs in sync

## Typical Workflow

```bash
# Document a new module
/document src/utils/helpers.js

# Copy the JSDoc comments into the source file
# Add the API reference to README.md
# Include usage examples in project documentation

# Later, when the module changes significantly
/document src/utils/helpers.js
# Review updated documentation for changes
```

## Best Practices

- **Document Early**: Create documentation as you write code
- **Keep Current**: Update documentation when APIs change
- **Be Detailed**: Include return types, error conditions, and examples
- **Use Examples**: Practical examples are worth a thousand words
- **Follow Standards**: Use JSDoc format for consistency
- **Document Purpose**: Explain "why" not just "what"
- **Note Edge Cases**: Document special conditions and limitations

## Output Format

Documentation is generated in a clear, readable format:
- ✅ Properly indented code examples
- ✅ Markdown-formatted sections
- ✅ Type information clearly specified
- ✅ Line numbers for reference
- ✅ Copy-paste ready code blocks
- ✅ Organized by category (classes, functions, utilities)

## Tips

- **For Classes**: Documents constructor, properties, and all methods
- **For Functions**: Includes parameter types, return values, and examples
- **For Utilities**: Explains purpose, usage patterns, and common scenarios
- **For APIs**: Creates complete reference documentation
- **For Modules**: Generates import/require instructions and integration guides

## See Also

- `/commit` - Create conventional commits after documenting changes
- `/test` - Generate tests to validate documented behavior
