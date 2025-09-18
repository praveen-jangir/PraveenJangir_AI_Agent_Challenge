# app.py

import streamlit as st
import google.generativeai as genai
import fitz  # PyMuPDF
import os

def get_text_from_pdf(pdf_file):
    """
    Extracts text from an uploaded PDF file.
    """
    try:
        # To read the uploaded file, we need to get its content in bytes
        file_bytes = pdf_file.getvalue()
        with fitz.open(stream=file_bytes, filetype="pdf") as doc:
            text = ""
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        st.error(f"Error reading PDF file: {e}")
        return None

def get_gemini_response(input_prompt):
    """
    Calls the Gemini Pro model and returns the response.
    """
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(input_prompt)
        return response.text
    except Exception as e:
        st.error(f"An error occurred with the AI model: {e}")
        # It's helpful to provide guidance on common errors like API key issues
        if "API_KEY_INVALID" in str(e):
            st.error("Your Google AI API key is invalid. Please check and enter a valid key.")
        return None

# --- Streamlit App Interface ---

# Configure the page
st.set_page_config(page_title="AI Resume Screening Agent", page_icon="📄", layout="wide")

# Header
st.title("🤖 AI Resume Screening Agent")
st.markdown("---")
st.markdown("""
Welcome to the AI Resume Screening Agent! This tool helps you quickly evaluate resumes against a job description. 
Follow the steps below to get started.
""")

# Sidebar for API Key Input
with st.sidebar:
    st.header("Configuration")
    google_api_key = st.text_input("Enter your Google AI API Key", type="password")
    if google_api_key:
        try:
            genai.configure(api_key=google_api_key)
            st.success("API Key configured successfully!", icon="✅")
        except Exception as e:
            st.error(f"Failed to configure API Key: {e}", icon="❌")

# Step 1: Job Description
st.header("Step 1: Provide the Job Description")
job_description = st.text_area("Paste the job description here (JD)", height=200, key="jd")

# Step 2: Resume Upload
st.header("Step 2: Upload Candidate Resumes")
uploaded_files = st.file_uploader(
    "Upload one or more resumes (PDF files only)",
    type=["pdf"],
    accept_multiple_files=True,
    key="resumes"
)

# Step 3: Analysis Button
st.header("Step 3: Analyze and Rank")
submit_button = st.button("Screen Resumes", type="primary")

# Processing and Displaying Results
if submit_button:
    if not google_api_key:
        st.warning("Please enter your Google AI API Key in the sidebar to proceed.")
    elif not job_description:
        st.warning("Please provide a job description.")
    elif not uploaded_files:
        st.warning("Please upload at least one resume.")
    else:
        with st.spinner("Analyzing resumes... This may take a moment. ⏳"):
            st.markdown("---")
            st.subheader("Analysis Results:")
            
            # The prompt template for the AI model
            input_prompt_template = """
            You are an expert HR professional with extensive experience in technical recruitment and talent acquisition. 
            Your task is to meticulously evaluate a candidate's resume against a given job description.

            Please provide the following:
            1.  **Match Score:** A percentage representing how well the resume matches the job description.
            2.  **Profile Summary:** A concise, professional summary of the candidate's profile based on their resume.
            3.  **Strengths & Alignment:** A brief analysis of what makes the candidate a strong fit for this role, highlighting key skills, experience, and qualifications that align directly with the job description.
            4.  **Potential Gaps:** Identify any noticeable gaps or areas where the candidate's experience does not align with the job requirements.

            **Job Description:**
            {jd}

            **Candidate's Resume:**
            {resume_text}

            ---
            **Output Format (Strict):**
            **Match Score:** [percentage]%
            **Profile Summary:** [summary]
            **Strengths & Alignment:** [analysis of strengths]
            **Potential Gaps:** [analysis of gaps]
            """
            
            for resume in uploaded_files:
                st.markdown(f"#### 📄 Candidate: {resume.name}")
                resume_text = get_text_from_pdf(resume)
                
                if resume_text:
                    # Format the prompt with the specific JD and resume text
                    formatted_prompt = input_prompt_template.format(jd=job_description, resume_text=resume_text)
                    
                    # Get the response from the Gemini model
                    response_text = get_gemini_response(formatted_prompt)
                    
                    if response_text:
                        with st.expander("Show Analysis Details", expanded=True):
                            st.markdown(response_text)
                    else:
                        st.error(f"Could not analyze the resume for {resume.name}.")
                else:
                    st.error(f"Failed to read the content of {resume.name}.")
                st.markdown("---")

# Footer in the sidebar
with st.sidebar:
    st.markdown("---")
    st.markdown("### About")
    st.markdown("This app is a demonstration for the **Rooman AI Agent Development Challenge**.")
    st.markdown("It uses Google's Gemini Pro model to analyze and rank resumes.")
