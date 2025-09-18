# AI Resume Screening Agent

This project is a submission for the Rooman AI Agent Development Challenge. It is a fully functional AI agent designed to solve the real-world problem of Resume Screening in the People & HR category.

---

## 📹 Demonstration Video

<video src="assets/demo.webm" controls width="700">
  Your browser does not support the video tag.
</video>

---

## 📷 Screenshots

![Screenshot 1](assets/screenshot1.png)  
![Screenshot 2](assets/screenshot2.png)  

---

## What The Agent Does

The **AI Resume Screening Agent** is a web-based application that helps HR professionals and hiring managers automate the initial phase of recruitment. It intelligently analyzes candidate resumes against a specific job description to identify the most qualified applicants quickly.

The user provides a job description and one or more resumes in PDF format. The agent then evaluates each resume and generates a detailed report that includes:

* A **match percentage** to quickly rank candidates.
* A **professional summary** of the candidate's profile.
* An analysis of the candidate's **strengths and alignment** with the role.
* A list of **potential gaps** or missing qualifications.

This saves significant time and effort, allowing recruitment teams to focus on the most promising candidates from the start.

---

## Key Features & Limitations

### ✅ Features

* **User-Friendly Interface:** Simple, clean, and intuitive UI built with Streamlit.
* **Multiple Resume Uploads:** Supports uploading and analyzing multiple PDF resumes simultaneously.
* **In-Depth Analysis:** Leverages the power of Google's Gemini Pro model for nuanced and context-aware analysis, going beyond simple keyword matching.
* **Structured Output:** Provides a clear, consistent, and easy-to-read report for each candidate.
* **Secure:** Requires the user to enter their own API key, which is not stored or logged.

### ⚠️ Limitations

* **PDF Only:** Currently, the agent only accepts resumes in PDF format.
* **Text Extraction Quality:** The analysis is highly dependent on the quality of text extraction from the PDF. Scanned or image-based PDFs will not work.
* **API Dependency:** Requires a valid and active Google AI API key to function. Performance depends on the API's availability.
* **No Data Storage:** The application is stateless. All uploaded data is processed in memory and discarded after the session ends.

---

## 🛠 Tools and APIs Used

* **AI Model:** Google Gemini  
* **UI Framework:** Streamlit  
* **Programming Language:** Python  
* **PDF Processing:** PyMuPDF (`fitz`) library  

---

## ⚙️ Setup Instructions 

To run this application on your local machine, follow these steps:

1. **Clone/Download the project files.**

2. **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. **Install the required Python libraries:**
    Create a file named `requirements.txt` with the following content:
    ```
    streamlit
    google-generativeai
    PyMuPDF
    ```
    Then run:
    ```bash
    pip install -r requirements.txt
    ```

4. **Get your Google AI API Key:**
    * Visit the Google AI Studio website.
    * Log in and create a new API key.

5. **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

6. **Use the Application:**
    * Enter your Google AI API key in the sidebar.
    * Paste the job description and upload resumes in PDF format.
    * View the analysis report.

---
