"""
{PROJECT_NAME} - FastAPI Main Application
"""
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

# Import API routers
from app.api import example

# Initialize FastAPI app
app = FastAPI(
    title="{PROJECT_NAME}",
    description="{PROJECT_DESCRIPTION}",
    version="0.1.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup static files and templates
BASE_DIR = Path(__file__).resolve().parent.parent
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# Include API routers
app.include_router(example.router, prefix="/api", tags=["example"])


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Main page"""
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "{PROJECT_NAME}"}
    )


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "{PROJECT_NAME}"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
