# AI-Generated-Portfolio-Website-from-Resume

# Overview

This project is an end-to-end AI application that automatically generates a professional portfolio website using a resume as the only input.
By integrating Streamlit, LangChain, and Google Gemini LLM, the system extracts resume content, structures it intelligently, and generates complete HTML, CSS, and JavaScript files ready for deployment.

The application eliminates the need for manual website design or formatting effort.

# System Architecture(Components)

Streamlit UI – User interface for resume upload and preview

Resume Extractor – PyPDF2 / python-docx

LLM #1 – Resume to structured website prompt

LLM #2 – Structured prompt to HTML/CSS/JS code

Website Preview Engine – Streamlit HTML component

ZIP Exporter – Packages website files for download

# Tech Stack

User Interface: Streamlit for building an interactive web-based UI

Document Parsing: PyPDF2 for PDF resumes and python-docx for DOCX resumes

LLM Integration: LangChain with Google Gemini API for prompt engineering and code generation

Backend Processing: Python for application logic and data handling

File Packaging: zipfile for bundling generated website files into a downloadable ZIP

Website Preview: Streamlit HTML component for rendering live website previews

Development Environment: Visual Studio Code (VS Code)

# Workflow

User uploads a PDF or DOCX resume through the Streamlit interface.

Resume content is extracted using PyPDF2 or python-docx.

An LLM converts the resume into a structured website specification (skills, experience, projects, education, design style).

A second LLM generates complete HTML, CSS, and JavaScript source code.

The generated website is rendered as a live preview within Streamlit.

All website files are packaged into a ZIP and made available for download.

# Use Cases

Job seekers and students

Data Analysts / ML Engineers / Developers

Rapid personal website generation

Resume-to-portfolio automation
