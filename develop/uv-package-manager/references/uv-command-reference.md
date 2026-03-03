# UV Command Reference

Comprehensive reference for uv commands, patterns, and workflows.

## Installation

### Quick Install

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Using pip (if you already have Python)
pip install uv

# Using Homebrew (macOS)
brew install uv

# Using cargo (if you have Rust)
cargo install --git https://github.com/astral-sh/uv uv
```

### Verify Installation

```bash
uv --version
```

## Virtual Environment Management

### Creating Virtual Environments

```bash
uv venv                          # Create virtual environment
uv venv --python 3.12            # With specific Python version
uv venv my-env                   # Custom name
uv venv --system-site-packages   # With system site packages
uv venv /path/to/venv            # Specify location
```

### Activating Virtual Environments

```bash
# Linux/macOS
source .venv/bin/activate

# Windows (Command Prompt)
.venv\Scripts\activate.bat

# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Or use uv run (no activation needed)
uv run python script.py
uv run pytest
```

### Using uv run

```bash
uv run python app.py                        # Run Python script (auto-activates venv)
uv run black .                               # Run installed CLI tool
uv run --python 3.11 python script.py        # Run with specific Python version
uv run python script.py --arg value          # Pass arguments
```

## Package Management

### Adding Dependencies

```bash
uv add requests                              # Add package
uv add "django>=4.0,<5.0"                   # With version constraint
uv add numpy pandas matplotlib              # Multiple packages
uv add --dev pytest pytest-cov              # Dev dependency
uv add --optional docs sphinx               # Optional dependency group
uv add git+https://github.com/user/repo.git # From git
uv add git+https://github.com/user/repo.git@v1.0.0  # Git with ref
uv add ./local-package                      # From local path
uv add -e ./local-package                   # Editable local package
```

### Removing Dependencies

```bash
uv remove requests                           # Remove package
uv remove --dev pytest                       # Remove dev dependency
uv remove numpy pandas matplotlib           # Remove multiple
```

### Upgrading Dependencies

```bash
uv add --upgrade requests                    # Upgrade specific package
uv sync --upgrade                            # Upgrade all packages
uv tree --outdated                           # Show what would be upgraded
```

### Locking Dependencies

```bash
uv lock                                      # Generate uv.lock file
uv lock --upgrade                            # Update lock file
uv lock --no-install                         # Lock without installing
uv lock --upgrade-package requests           # Lock specific package
```

## Python Version Management

### Installing Python Versions

```bash
uv python install 3.12                       # Install Python version
uv python install 3.11 3.12 3.13            # Install multiple versions
uv python install                            # Install latest version
uv python list                               # List installed versions
uv python list --all-versions               # Find available versions
```

### Setting Python Version

```bash
uv python pin 3.12                           # Set Python version for project
uv --python 3.11 run python script.py        # Use specific version for command
uv venv --python 3.12                        # Create venv with specific version
```

## Project Configuration

### pyproject.toml with uv

```toml
[project]
name = "my-project"
version = "0.1.0"
description = "My awesome project"
readme = "README.md"
requires-python = ">=3.8"
dependencies = [
    "requests>=2.31.0",
    "pydantic>=2.0.0",
    "click>=8.1.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.0",
    "pytest-cov>=4.1.0",
    "black>=23.0.0",
    "ruff>=0.1.0",
    "mypy>=1.5.0",
]
docs = [
    "sphinx>=7.0.0",
    "sphinx-rtd-theme>=1.3.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.uv]
dev-dependencies = []

[tool.uv.sources]
my-package = { git = "https://github.com/user/repo.git" }
```

### Using uv with Existing Projects

```bash
uv add -r requirements.txt                  # Migrate from requirements.txt
uv sync                                     # Migrate from poetry (with pyproject.toml)
uv pip freeze > requirements.txt             # Export to requirements.txt
uv pip freeze --require-hashes > requirements.txt  # Export with hashes
```

## Advanced Workflows

### Monorepo Support

```bash
# Root pyproject.toml
[tool.uv.workspace]
members = ["packages/*"]

# Install all workspace packages
uv sync

# Add workspace dependency
uv add --path ./packages/package-a
```

### CI/CD Integration

```yaml
# .github/workflows/test.yml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Install uv
        uses: astral-sh/setup-uv@v2
        with:
          enable-cache: true
      - name: Set up Python
        run: uv python install 3.12
      - name: Install dependencies
        run: uv sync --all-extras --dev
      - name: Run tests
        run: uv run pytest
      - name: Run linting
        run: |
          uv run ruff check .
          uv run black --check .
```

### Docker Integration

```dockerfile
# Simple Dockerfile
FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev
COPY . .
CMD ["uv", "run", "python", "app.py"]
```

**Optimized multi-stage build:**

```dockerfile
FROM python:3.12-slim AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev --no-editable

FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /app/.venv .venv
COPY . .
ENV PATH="/app/.venv/bin:$PATH"
CMD ["python", "app.py"]
```

### Lockfile Workflows

```bash
uv lock                                      # Create lockfile
uv sync --frozen                             # Install from lockfile (exact versions)
uv lock --no-install                         # Update lockfile without installing
uv lock --upgrade-package requests           # Upgrade specific package in lock
uv lock --check                              # Check if lockfile is up to date
uv export --format requirements-txt > requirements.txt  # Export lockfile
uv export --format requirements-txt --hash > requirements.txt  # Export with hashes
```

## Performance Optimization

### Global Cache

```bash
# UV automatically uses global cache at:
# Linux: ~/.cache/uv
# macOS: ~/Library/Caches/uv
# Windows: %LOCALAPPDATA%\uv\cache

uv cache clean                               # Clear cache
uv cache dir                                 # Check cache location
```

### Parallel Installation

```bash
uv pip install --jobs 4 package1 package2    # Control parallelism
uv pip install --jobs 1 package              # Sequential
```

### Offline Mode

```bash
uv pip install --offline package             # Install from cache only
uv sync --frozen --offline                   # Sync from lockfile offline
```

## Comparison with Other Tools

### uv vs pip
```bash
# pip: ~30 seconds
python -m venv .venv && source .venv/bin/activate && pip install requests pandas numpy

# uv: ~2 seconds (10-15x faster)
uv venv && uv add requests pandas numpy
```

### uv vs poetry
```bash
# poetry: ~20 seconds
poetry init && poetry add requests pandas && poetry install

# uv: ~3 seconds (6-7x faster)
uv init && uv add requests pandas && uv sync
```

### uv vs pip-tools
```bash
# pip-tools: ~15 seconds
pip-compile requirements.in && pip-sync requirements.txt

# uv: ~2 seconds (7-8x faster)
uv lock && uv sync --frozen
```

## Common Workflows

### Starting a New Project

```bash
uv init my-project && cd my-project
uv python pin 3.12
uv add fastapi uvicorn pydantic
uv add --dev pytest black ruff mypy
mkdir -p src/my_project tests
uv run pytest
uv run black . && uv run ruff check .
```

### Maintaining Existing Project

```bash
git clone https://github.com/user/project.git && cd project
uv sync                                      # Install dependencies
uv sync --all-extras                         # With dev dependencies
uv lock --upgrade                            # Update dependencies
uv run python app.py                         # Run application
uv add new-package                           # Add new dependency
git add pyproject.toml uv.lock && git commit -m "Add new-package dependency"
```

## Tool Integration

### Pre-commit Hooks

```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: uv-lock
        name: uv lock
        entry: uv lock
        language: system
        pass_filenames: false
      - id: ruff
        name: ruff
        entry: uv run ruff check --fix
        language: system
        types: [python]
      - id: black
        name: black
        entry: uv run black
        language: system
        types: [python]
```

### VS Code Integration

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "python.terminal.activateEnvironment": true,
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": ["-v"],
  "python.linting.enabled": true,
  "python.formatting.provider": "black",
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true
  }
}
```

## Troubleshooting

```bash
# uv not found - Add to PATH
echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> ~/.bashrc

# Wrong Python version - Pin explicitly
uv python pin 3.12
uv venv --python 3.12

# Dependency conflict - Check resolution
uv lock --verbose

# Cache issues - Clear cache
uv cache clean

# Lockfile out of sync - Regenerate
uv lock --upgrade
```

## Migration Guide

### From pip + requirements.txt
```bash
uv venv
uv pip install -r requirements.txt
# Or better:
uv init && uv add -r requirements.txt
```

### From Poetry
```bash
uv sync
uv add requests
# Keep existing pyproject.toml - uv reads [project] and [tool.poetry]
```

### From pip-tools
```bash
uv lock
uv sync --frozen
```

## Essential Commands

```bash
# Project management
uv init [PATH]              # Initialize project
uv add PACKAGE              # Add dependency
uv remove PACKAGE           # Remove dependency
uv sync                     # Install dependencies
uv lock                     # Create/update lockfile

# Virtual environments
uv venv [PATH]              # Create venv
uv run COMMAND              # Run in venv

# Python management
uv python install VERSION   # Install Python
uv python list              # List installed Pythons
uv python pin VERSION       # Pin Python version

# Package installation (pip-compatible)
uv pip install PACKAGE      # Install package
uv pip uninstall PACKAGE    # Uninstall package
uv pip freeze               # List installed
uv pip list                 # List packages

# Utility
uv cache clean              # Clear cache
uv cache dir                # Show cache location
uv --version                # Show version
```

## Resources

- **Official documentation**: https://docs.astral.sh/uv/
- **GitHub repository**: https://github.com/astral-sh/uv
- **Astral blog**: https://astral.sh/blog
- **Migration guides**: https://docs.astral.sh/uv/guides/
- **Comparison with other tools**: https://docs.astral.sh/uv/pip/compatibility/

## Best Practices Summary

1. **Use uv for all new projects** - Start with `uv init`
2. **Commit lockfiles** - Ensure reproducible builds
3. **Pin Python versions** - Use .python-version
4. **Use uv run** - Avoid manual venv activation
5. **Leverage caching** - Let uv manage global cache
6. **Use --frozen in CI** - Exact reproduction
7. **Keep uv updated** - Fast-moving project
8. **Use workspaces** - For monorepo projects
9. **Export for compatibility** - Generate requirements.txt when needed
10. **Read the docs** - uv is feature-rich and evolving
