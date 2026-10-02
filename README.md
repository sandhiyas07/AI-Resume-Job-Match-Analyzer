# AI Resume & Job Match Analyzer

## Overview

AI Resume & Job Match Analyzer is an AI-powered application that analyzes a resume against a given job description and identifies how well the candidate matches the job requirements.

The application extracts important skills and keywords from the resume and job description, compares them, and provides a job match score along with matched skills and missing skills.

## Features

* Upload and analyze a resume
* Enter a job description
* Extract skills and keywords
* Compare resume skills with job requirements
* Generate a job match score
* Display matched skills
* Identify missing skills
* Provide simple improvement suggestions
* User-friendly interface
* Helps candidates understand their job readiness

## How It Works

The application follows these basic steps:

1. Upload your resume.
2. Enter or paste the job description.
3. The system analyzes the resume.
4. The system analyzes the job description.
5. Required skills are identified.
6. Resume skills are compared with job requirements.
7. A match score is calculated.
8. Matched and missing skills are displayed.
9. Suggestions are provided to improve the resume.

## Technologies Used

* Python
* Streamlit
* Natural Language Processing
* Machine Learning
* Pandas
* Regular Expressions
* PDF Processing
* HTML
* CSS

## Project Structure

```text
AI-Resume-Job-Match-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   └── sample_job_description.txt
│
├── uploads/
│   └── .gitkeep
│
└── screenshots/
    └── demo.png
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/AI-Resume-Job-Match-Analyzer.git
```

### 2. Open the Project Folder

```bash
cd AI-Resume-Job-Match-Analyzer
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

## Example Job Description

```text
We are looking for a Software Developer with knowledge of Python,
HTML, CSS, JavaScript, React.js, Git and SQL.

The candidate should have good problem-solving and communication skills.
```

## Example Skills

The application can analyze skills such as:

* Python
* Java
* JavaScript
* HTML
* CSS
* React.js
* SQL
* Git
* GitHub
* Machine Learning
* Data Science
* Communication
* Problem Solving

## Output

The application provides:

### Match Score

Shows the percentage of similarity between the resume and job description.

### Matched Skills

Displays skills that are present in both the resume and the job description.

### Missing Skills

Displays important skills mentioned in the job description but not found in the resume.

### Suggestions

Provides suggestions for improving the resume based on the missing skills.

## Use Cases

* Resume analysis
* Job preparation
* Skill gap identification
* Career planning
* Resume improvement
* Job application preparation

## Future Enhancements

* AI-powered resume recommendations
* Multiple resume formats
* Job recommendation system
* LinkedIn profile analysis
* Resume keyword optimization
* ATS compatibility analysis
* Multiple job description comparison
* Advanced NLP-based semantic matching
* Resume improvement suggestions using Generative AI

## Advantages

* Easy to use
* Saves time during job preparation
* Helps identify missing skills
* Provides a clear job match score
* Useful for students and freshers
* Helps improve resume relevance

## Screenshots

Add your project screenshots here after running the application.

```text
screenshots/
└── demo.png
```

You can display a screenshot in this README using:

```markdown
![AI Resume & Job Match Analyzer](screenshots/demo.png)
```

## Demo Video

Add your project demonstration video link here:

```text
Demo Video:
```

## Author

**Sandhiya**

B.Tech – Artificial Intelligence and Data Science

## License

This project is created for educational and portfolio purposes.
