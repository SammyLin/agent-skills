---
name: fastapi-generator
description: Generate FastAPI project scaffolding with TailwindCSS and Alpine.js frontend. Use when needing to quickly create a new API service with modern dark-themed UI, CORS support, static files, and example endpoints. Saves ~7k tokens by providing battle-tested boilerplate instead of writing from scratch. Do not use for: Django/Flask/Express projects, modifying existing FastAPI apps, frontend-only projects, or MCP server creation (use mcp-builder).
---

# FastAPI Project Generator

Quickly generate a complete FastAPI project with TailwindCSS + Alpine.js frontend.

## What You Get

A fully functional FastAPI project with:

- **FastAPI backend** - Modern async web framework
- **Dark theme UI** - TailwindCSS + Alpine.js
- **Example API** - CRUD endpoints with in-memory storage
- **CORS enabled** - Ready for frontend integration
- **Auto documentation** - Swagger UI and ReDoc
- **Health check** - `/health` endpoint
- **Project structure** - Organized and ready to extend

## Usage

Generate a new project:

```bash
python scripts/generate_project.py my-api
```

With custom description:

```bash
python scripts/generate_project.py my-api --description "Stock trading API"
```

To a specific directory:

```bash
python scripts/generate_project.py my-api --output ~/projects
```

Without Git initialization:

```bash
python scripts/generate_project.py my-api --no-git
```

## Generated Structure

```
my-api/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app with CORS, static files
│   └── api/
│       ├── __init__.py
│       └── example.py       # Example CRUD endpoints
├── templates/
│   └── index.html           # Dark theme UI (TailwindCSS + Alpine.js)
├── static/
│   └── css/
├── requirements.txt         # Core dependencies (FastAPI, Uvicorn, etc.)
├── .gitignore
└── README.md
```

## Next Steps After Generation

1. **Setup environment:**
   ```bash
   cd my-api
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Run the server:**
   ```bash
   python -m app.main
   ```

3. **Access:**
   - Homepage: http://localhost:8000
   - API Docs: http://localhost:8000/docs
   - Health: http://localhost:8000/health

## Customization Points

After generation, commonly customize:

1. **API endpoints** - Modify `app/api/example.py` or add new routers
2. **Database** - Add SQLAlchemy or other ORM to `requirements.txt` and models
3. **Authentication** - Add JWT or OAuth middleware
4. **Frontend** - Modify `templates/index.html` with your UI
5. **Static assets** - Add CSS/JS/images to `static/`

## When to Use

Use this skill when:

- Starting a new FastAPI project
- Need a quick prototype with UI
- Want a dark-themed dashboard/admin panel
- Building an API that needs a frontend interface
- Tired of rewriting the same FastAPI boilerplate

## Token Savings

Estimated **~7k tokens saved** per use by providing:
- Pre-configured FastAPI app with CORS
- Dark theme UI template
- Example CRUD endpoints
- Proper project structure
- Requirements file

Instead of describing these requirements and having them generated each time, use this skill.
