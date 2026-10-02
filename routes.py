from pathlib import Path

from fastapi import APIRouter, File, Form, Request, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.resume_parser import extract_text_from_pdf
from app.gemini_service import analyze_resume


router = APIRouter()

BASE_DIR = Path(__file__).resolve().parent.parent

UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

TEMPLATES_DIR = BASE_DIR / "templates"

templates = Jinja2Templates(directory=str(TEMPLATES_DIR))


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={}
    )


@router.post("/analyze")
async def analyze(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):

    if not resume.filename:
        return {
            "success": False,
            "message": "Please select a resume PDF."
        }

    if not resume.filename.lower().endswith(".pdf"):
        return {
            "success": False,
            "message": "Please upload a PDF file only."
        }

    file_path = UPLOAD_DIR / resume.filename

    content = await resume.read()

    with open(file_path, "wb") as file:
        file.write(content)

    try:

        resume_text = extract_text_from_pdf(file_path)

        if not resume_text:
            return {
                "success": False,
                "message": "Could not extract text from the PDF."
            }

        result = analyze_resume(
            resume_text,
            job_description
        )

        return {
            "success": True,
            "result": result
        }

    except Exception as error:

        return {
            "success": False,
            "message": str(error)
        }