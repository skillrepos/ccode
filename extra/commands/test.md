---
description: "Generate tests based on type (unit, integration, e2e)"
argument-hint: "[unit | integration | e2e]"
---

# Generate Tests by Type

Generate appropriate test code based on the specified test type (unit, integration, or e2e).

## Command Syntax

```
/test <type>
```

## Arguments

- **type** (required): One of the following:
  - `unit` - Generate unit tests for individual functions/methods
  - `integration` - Generate integration tests for component interactions
  - `e2e` - Generate end-to-end tests for complete user workflows

## Examples

```
/test unit
/test integration
/test e2e
```

## What Each Test Type Generates

### Unit Tests (`/test unit`)
Focused tests for individual components in isolation:
- Single method/function testing
- Input validation scenarios
- Return value verification
- Error handling for single units
- Edge cases and boundary conditions
- Mocking external dependencies

### Integration Tests (`/test integration`)
Tests for multiple components working together:
- Component interaction flows
- Data passing between modules
- State management across components
- Cross-module communication
- Dependency integration
- Setup and teardown for multi-component scenarios

### End-to-End Tests (`/test e2e`)
Complete workflow tests simulating real user scenarios:
- Full application flows
- User journey scenarios
- Multiple steps in sequence
- Real-world data flows
- External service integration
- Complete state transitions

## Generated Output

Each command generates a test file template with:
- Appropriate setup/teardown for the test type
- Sample test cases demonstrating best practices
- Descriptive comments explaining the structure
- Proper assertion patterns
- Error handling examples
- Configuration for the test framework (Jest, Mocha, Cypress, etc.)

## Integration with Claude Code

This command analyzes your codebase and generates contextual tests tailored to:
- Your existing code structure
- Current test patterns
- Project dependencies
- Testing framework in use
