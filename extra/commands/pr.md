# Pull Request Workflow

Create a feature branch, make changes, commit with conventional commit messages, and create a pull request.

## Workflow Steps

Follow these steps to create a complete pull request:

### 1. Create Feature Branch
- Check current branch status
- Create a new feature branch with descriptive name (e.g., `feature/user-authentication`, `fix/email-validation`, `refactor/api-endpoints`)
- Switch to the new branch

### 2. Make Changes
- Identify what changes need to be made based on the feature or fix
- Implement the changes across relevant files
- Ensure code follows the project's style guide (JavaScript, Prettier, ESLint)

### 3. Commit with Conventional Commit Messages
Use conventional commit format: `<type>(<scope>): <description>`

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `refactor`: Code refactoring
- `docs`: Documentation changes
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `style`: Code style changes (formatting)
- `perf`: Performance improvements

**Examples:**
- `feat(auth): add user login endpoint`
- `fix(validation): correct email regex pattern`
- `refactor(user): simplify User class methods`
- `test(user): add edge case tests for setEmail`

**Commit Message Format:**
```
<type>(<scope>): <short description>

<optional longer description>

<optional footer with breaking changes or issue references>
```

### 4. Push and Create Pull Request
- Push the feature branch to remote
- Create a pull request with:
  - **Title**: Clear, descriptive summary of changes
  - **Description**: Include:
    - Summary of changes
    - Motivation for the changes
    - Testing performed
    - Any breaking changes
    - Related issue numbers

## Pull Request Description Template

```markdown
## Summary
Brief description of what this PR does.

## Changes
- List of specific changes made
- Another change
- etc.

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Refactoring (no functional changes)

## Testing
- Describe tests performed
- Test results
- Edge cases covered

## Checklist
- [ ] Code follows project style guidelines
- [ ] Tests added/updated and passing
- [ ] Documentation updated (if needed)
- [ ] No breaking changes (or documented)
- [ ] Commits follow conventional commit format

## Related Issues
Closes #[issue number]
```

## Execution

Now execute this workflow:

1. **Check git status** and current branch
2. **Ask user** for feature branch name if not specified
3. **Create and switch** to feature branch
4. **Implement changes** based on user requirements
5. **Stage and commit** with proper conventional commit message
6. **Push branch** to remote
7. **Generate PR description** using the template above
8. **Create pull request** using `gh pr create` (if gh CLI is available)

After each step, inform the user of progress and any actions taken.
