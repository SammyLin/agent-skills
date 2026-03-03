# Git Commit Conventions Reference

## Commit Message Examples

**Feature commit:**
```
feat(auth): add JWT authentication

Implement JWT-based authentication system with:
- Login endpoint with token generation
- Token validation middleware
- Refresh token support
```

**Bug fix:**
```
fix(api): handle null values in user profile

Prevent crashes when user profile fields are null.
Add null checks before accessing nested properties.
```

**Refactor:**
```
refactor(database): simplify query builder

Extract common query patterns into reusable functions.
Reduce code duplication in database layer.
```

## Multi-file Commits

```
refactor(core): restructure authentication module

- Move auth logic from controllers to service layer
- Extract validation into separate validators
- Update tests to use new structure
- Add integration tests for auth flow

Breaking change: Auth service now requires config object
```

## Scope Examples

**Frontend:**
- `feat(ui): add loading spinner to dashboard`
- `fix(form): validate email format`

**Backend:**
- `feat(api): add user profile endpoint`
- `fix(db): resolve connection pool leak`

**Infrastructure:**
- `chore(ci): update Node version to 20`
- `feat(docker): add multi-stage build`

## Breaking Changes

```
feat(api)!: restructure API response format

BREAKING CHANGE: All API responses now follow JSON:API spec

Previous format:
{ "data": {...}, "status": "ok" }

New format:
{ "data": {...}, "meta": {...} }

Migration guide: Update client code to handle new response structure
```

## Commit Message Checklist

- [ ] Type is appropriate (feat/fix/docs/etc.)
- [ ] Scope is specific and clear
- [ ] Summary is under 50 characters
- [ ] Summary uses imperative mood
- [ ] Body explains WHY not just WHAT
- [ ] Breaking changes are clearly marked
- [ ] Related issue numbers are included

## Amending Commits

```bash
git commit --amend                  # Amend message only
git add forgotten-file.js
git commit --amend --no-edit        # Amend and add changes
```

## Interactive Staging

```bash
git add -p                          # Stage changes interactively
git diff --staged                   # Review what's staged
git commit -m "type(scope): description"
```
