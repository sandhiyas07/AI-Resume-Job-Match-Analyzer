from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routes import router


BASE_DIR = Path(__file__).resolve().parent.parent

app = FastAPI(
    title="AI Resume & Job Match Analyzer",
    version="1.0.0"
)

# Static files
app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)

# Templates
templates = Jinja2Templates(
    directory=BASE_DIR / "templates"
)

# Routes
app.include_router(router)


@app.get("/health")
def health_check():
    return {
        "status": "success",
        "message": "AI Resume & Job Match Analyzer is running!"
    }