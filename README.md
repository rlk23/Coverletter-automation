# AI-Powered Cover Letter Generator

## Introduction

The **AI-Powered Cover Letter Generator** is an open-source project designed to simplify the job application process. It leverages advanced language models (LLMs) like ChatGPT to generate tailored cover letters based on your resume and the specific job description you provide. The generated cover letter is downloadable as a Word document, making it ready for submission.

## Features

- **Automated Cover Letter Creation**: Generates a professional and personalized cover letter aligned with the job requirements.
- **Resume Upload**: Accepts resume uploads in PDF or DOCX formats for parsing and analysis.
- **Job Description Analysis**: Uses the provided job posting link to understand the role's requirements and tailor the cover letter accordingly.
- **Output as Word Document**: Provides the generated cover letter in `.docx` format for easy download and use.
- **Web Interface**: User-friendly interface built with Flask.

## How It Works

1. **Input**:
   - Upload your resume.
   - Provide the job posting link.
   - Enter your OpenAI API key for LLM integration.
2. **Processing**:
   - The application analyzes your resume and extracts key details from the job posting.
   - Using OpenAI’s API, it generates a customized cover letter based on the role requirements.
3. **Output**:
   - The generated cover letter is saved as a Word document, ready for download.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- OpenAI API key
- Required Python libraries (see `requirements.txt`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-cover-letter-generator.git
   cd ai-cover-letter-generator
