---
name: uv-package-manager
description: Master the uv package manager for fast Python dependency management, virtual environments, and modern Python project workflows. Use when setting up Python projects, managing dependencies, or optimizing Python development workflows with uv. Do not use for: npm/yarn/pnpm JavaScript package management, conda environments, Docker container management, or non-Python language toolchains.
---

# UV Package Manager

Comprehensive guide to using uv, an extremely fast Python package installer and resolver written in Rust.

## Core Concepts

- **Ultra-fast package installer**: 10-100x faster than pip, written in Rust
- **Drop-in pip replacement**: Compatible with pip workflows
- **Virtual environment manager**: Create and manage venvs
- **Python installer**: Download and manage Python versions
- **Lockfile support**: Reproducible installations
- **Global cache**: Disk space efficient

### UV vs Traditional Tools

- **vs pip**: 10-100x faster, better resolver
- **vs pip-tools**: Faster, simpler, better UX
- **vs poetry**: Faster, less opinionated, lighter

## Quick Start

```bash
# Create new project
uv init my-project
cd my-project

# Install dependencies
uv add requests pandas
uv add --dev pytest black ruff

# Run commands (no venv activation needed)
uv run python app.py
uv run pytest

# Sync from lockfile
uv sync
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

# pip-compatible
uv pip install PACKAGE      # Install package
uv pip freeze               # List installed

# Utility
uv cache clean              # Clear cache
uv --version                # Show version
```

## Best Practices

1. **Always use lockfiles** for reproducibility
2. **Pin Python version** with .python-version
3. **Use uv run** instead of activating venv
4. **Commit uv.lock** to version control
5. **Use --frozen in CI** for consistent builds
6. **Use workspaces** for monorepos

## Detailed Reference

For comprehensive command reference, advanced workflows (CI/CD, Docker, monorepo), migration guides, configuration examples, and troubleshooting, see [references/uv-command-reference.md](references/uv-command-reference.md).

## Resources

- **Official documentation**: https://docs.astral.sh/uv/
- **GitHub repository**: https://github.com/astral-sh/uv
