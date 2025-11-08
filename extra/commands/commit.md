---
description: "Stage changes, run tests, and create a conventional commit"
argument-hint: "[message]"
---

# Create Conventional Commit

Stages all changes, runs tests to ensure quality, and creates a commit with conventional commit message format.

## Command Syntax

```
/commit <message>
```

## Arguments

- **message** (required): The commit message describing the changes
  - Will be automatically formatted as conventional commit
  - Should be concise and descriptive (e.g., "add user validation", "fix email regex")
  - Optionally prefix with type: `feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `perf:`, `chore:`
  - If no type prefix, defaults to `feat:` for new features or `fix:` for bug fixes

## Examples

```
/commit "add email validation tests"
/commit "feat: implement password hashing"
/commit "fix: correct regex pattern for email validation"
/commit "docs: update README with API documentation"
/commit "test: add unit tests for User class"
/commit "refactor: simplify email validation logic"
```

## What This Command Does

### 1. Check Git Status
- Verifies there are changes to commit
- Lists all staged and unstaged changes

### 2. Stage Changes
- Stages all modified files (`git add .`)
- Excludes untracked files by default
- Option to include specific untracked files if needed

### 3. Run Tests
- Executes test suite (`npm test` or `node test-user.js`)
- Validates that all tests pass before committing
- Blocks commit if tests fail to prevent broken builds
- Shows test results summary

### 4. Create Conventional Commit
- Formats message according to [Conventional Commits](https://www.conventionalcommits.org/) spec
- Types: `feat`, `fix`, `docs`, `test`, `refactor`, `perf`, `chore`
- Format: `<type>(<scope>): <description>`
- Includes scopes when applicable (e.g., `feat(auth): add password validation`)
- Auto-detects type if not specified

### 5. Push Option
- Offers to push to remote after commit
- Uses tracked branch or origin/main by default
- Optional step, can commit without pushing

## Conventional Commit Types

| Type | Meaning | When to Use |
|------|---------|-----------|
| `feat` | New feature | Adding new functionality |
| `fix` | Bug fix | Correcting existing code |
| `docs` | Documentation | README, comments, guides |
| `test` | Tests | Adding or updating tests |
| `refactor` | Code refactoring | Improving code without changing behavior |
| `perf` | Performance | Optimizing code |
| `chore` | Maintenance | Dependencies, build tools, config |

## Features

- **Test-First**: Ensures tests pass before creating commits
- **Consistent Messages**: Enforces conventional commit format
- **Safety Checks**: Prevents committing with failing tests
- **Smart Detection**: Auto-detects commit type based on changes
- **Clean History**: Maintains clear, searchable git history
- **Interactive**: Options to review changes before committing

## Workflow Integration

Typical usage flow:
```bash
# Make code changes
# Run tests locally if needed
/commit "feat: add new validation function"
# Review the commit that was created
git log -1  # View the created commit
```

This ensures:
- ✅ All tests pass
- ✅ Changes are properly staged
- ✅ Commit message is clear and searchable
- ✅ Git history is clean and conventional
- ✅ Team can understand change purpose at a glance

## Tips

- **Be specific**: Use scopes to indicate what was changed (e.g., `feat(auth):`, `fix(email):`)
- **Keep messages short**: First line should be ~50 characters
- **Add details in body**: Use multiline commits for complex changes
- **Use imperative mood**: "add feature" not "added feature"
- **Reference issues**: Include issue numbers when applicable (e.g., `fix: resolve login bug (#123)`)
