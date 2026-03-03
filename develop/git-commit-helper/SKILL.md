---
name: Git Commit Helper
description: Generate descriptive commit messages by analyzing git diffs. Use when the user asks for help writing commit messages or reviewing staged changes. Do not use for: git branching strategies, merge conflict resolution, CI/CD pipeline configuration, or general git tutorials.
hooks:
  PostToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "echo \"[$(date)] Git Commit Helper: Analyzed git diff for commit message\" >> ~/.claude/git-commit-helper.log"
---

# Git Commit Helper

## Quick start

Analyze staged changes and generate commit message:

```bash
git diff --staged        # View staged changes
git diff --staged --stat # Show statistics
```

## Commit message format

Follow conventional commits:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting)
- **refactor**: Code refactoring
- **test**: Adding or updating tests
- **chore**: Maintenance tasks

## Commit message guidelines

**DO:**
- Use imperative mood ("add feature" not "added feature")
- Keep first line under 50 characters
- Capitalize first letter; no period at end
- Explain WHY not just WHAT in body

**DON'T:**
- Use vague messages like "update" or "fix stuff"
- Include implementation details in summary
- Mix unrelated changes

## Template workflow

1. **Review changes**: `git diff --staged`
2. **Identify type**: feat, fix, refactor, etc.
3. **Determine scope**: What part of the codebase?
4. **Write summary**: Brief, imperative description
5. **Add body**: Explain why and what impact
6. **Note breaking changes**: If applicable

## Best practices

1. **Atomic commits** - One logical change per commit
2. **Test before commit** - Ensure code works
3. **Reference issues** - Include issue numbers if applicable
4. **Keep it focused** - Don't mix unrelated changes

## Detailed Reference

For commit message examples, scope examples, breaking change format, multi-file commit patterns, and the full checklist, see [references/commit-conventions.md](references/commit-conventions.md).
