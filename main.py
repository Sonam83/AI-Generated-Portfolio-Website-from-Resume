import streamlit as st 
import dotenv
import langchain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv() 
import os
os.environ["GOOGLE_API_KEY"]=os.getenv("gemini")
import zipfile
import PyPDF2
import docx

st.set_page_config(page_title="Portfolio from Resume",page_icon="🤖")
st.title("AI Generated Portfolio Website from Resume")

# -----------------------------Uploading Resumes-----------------------------------------
with st.form(key="Resume"):
    name=st.text_input("Enter Your Name:")
    resume=st.file_uploader("Upload Resume (PDF / DOCX)",type=["pdf", "docx"])
    design_style = st.selectbox("Select Design Style",["Minimal", "Modern", "Creative", "Dark Theme"])
    submit=st.form_submit_button("Generate Portfolio",icon="🔥")

# --------------------------------Extracting text-------------------------------------------
def extract_resume_text(resume):
    if resume.type=="application/pdf":
        reader=PyPDF2.PdfReader(resume)
        text=""
        for page in reader.pages:
            text +=page.extract_text()
        return text

    elif resume.type=="application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        document=docx.Document(resume)
        return "\n".join([para.text for para in document.paragraphs])

    return ""

# ----------------------for LLM's-------------------------------------------------------------------
if submit and resume:
    
    with st.spinner("📄 Extracting resume content..."):
        resume_text = extract_resume_text(resume)

    #LLM1:content extraction for portfolio
    with st.spinner("🧠 Analyzing resume..."):
        content_prompt=extract_resume_text(resume)

    # ---------------- LLM #1 : CONTENT EXTRACTION ---------------- #
    with st.spinner("🧠 Analyzing resume..."):
        content_prompt = f"""
        You are an AI resume analyst.

        From the resume below, extract:
        - Name
        - Skills
        - Experience
        - Projects
        - Achievements
        - Education

        Resume:
        {resume_text}

        Return clean structured content for a portfolio website.
        """

        model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
        structured_content = model.invoke(content_prompt).content

    # --------------LLM2 : Website  sourcecode------------------------------------------
    with st.spinner("💻 Generating website source code..."):
        website_prompt = f"""
        You are an expert frontend developer.

        Using the content below, generate a portfolio website.
        Design Style: {design_style}

        Content:
        {structured_content}

        Output must be strictly in this format:

        ---html---
        [HTML CODE ONLY]
        ---html---

        ---css---
        [CSS CODE ONLY]
        ---css---

        ---java script---
        [JAVASCRIPT CODE ONLY]
        ---java script---
        """

        response = model.invoke(website_prompt).content

    #---------------------file generation------------------------------
    html_code = response.split("---html---")[1]
    css_code = response.split("---css---")[1]
    js_code = response.split("---java script---")[1]

    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_code)

    with open("style.css", "w", encoding="utf-8") as f:
        f.write(css_code)

    with open("script.js", "w", encoding="utf-8") as f:
        f.write(js_code)

     # ---------------- ZIP CREATION ---------------- #
    with zipfile.ZipFile("portfolio_website.zip", "w") as zipf:
        zipf.write("index.html")
        zipf.write("style.css")
        zipf.write("script.js")

    # ---------------- PREVIEW ---------------- #
    st.success("✅ Portfolio Website Generated Successfully!")
    st.subheader("🌐 Live Website Preview")
    st.components.v1.html(html_code, height=600, scrolling=True)

    # ---------------- DOWNLOAD ---------------- #
    with open("portfolio_website.zip", "rb") as f:
        st.download_button("⬇️ Download Portfolio Website (ZIP)",data=f,file_name="portfolio_website.zip",mime="application/zip")

