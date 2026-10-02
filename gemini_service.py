import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is missing. "
        "Please add your Gemini API key to the .env file."
    )

client = genai.Client(api_key=GEMINI_API_KEY)


def analyze_resume(resume_text: str, job_description: str) -> str:
    prompt = f"""
You are an AI Resume and Job Match Analyzer.

Analyze the candidate's resume against the given job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Provide the result in the following format:

1. MATCH PERCENTAGE
Give an estimated percentage from 0 to 100 based only on the skills,
experience, education, and requirements visible in the provided text.

2. MATCHING SKILLS
List the skills present in both the resume and job description.

3. MISSING SKILLS
List important job-related skills mentioned in the job description
that are not clearly present in the resume.

4. RESUME STRENGTHS
List the strongest relevant points found in the resume.

5. IMPROVEMENT SUGGESTIONS
Give practical suggestions for improving the resume for this job.

6. INTERVIEW QUESTIONS
Generate 5 relevant interview questions based on the job description
and the candidate's resume.

Keep the response clear, professional, and easy to understand.
Do not invent qualifications or experience that are not present.
"""

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    return response.text