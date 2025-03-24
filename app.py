import os
import fitz  # PyMuPDF for PDF handling
import docx
import pytesseract  # OCR for image extraction
import joblib
import pandas as pd
import streamlit as st
from PIL import Image
from io import BytesIO
from sklearn.pipeline import Pipeline
import numpy as np

# Load the trained model
pipeline: Pipeline = joblib.load("model.pkl")  # Ensure model.pkl exists

# Function to extract text from PDF
def extract_text_from_pdf(uploaded_file):
    """Extract text from a PDF file uploaded via Streamlit."""
    try:
        # Read the file as bytes
        pdf_data = uploaded_file.read()

        # Open the PDF document correctly
        doc = fitz.open(stream=pdf_data, filetype="pdf")

        # Extract text from all pages
        text = ""
        for page in doc:
            text += page.get_text("text") + "\n"

        doc.close()
        return text.strip()

    except Exception as e:
        return f"Error extracting text: {e}"

# Function to extract text from DOCX
def extract_text_from_docx(uploaded_file):
    """Extracts text from an uploaded DOCX file."""
    doc = docx.Document(uploaded_file)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text.strip()

# Function to extract text from images (JPG, PNG)
def extract_text_from_image(uploaded_file):
    """Extracts text from an uploaded image using OCR."""
    img = Image.open(uploaded_file)
    text = pytesseract.image_to_string(img)
    return text.strip()

# Function to process uploaded resumes
def process_resume(uploaded_file):
    file_extension = uploaded_file.name.split(".")[-1].lower()
    text = ""

    if file_extension == "pdf":
        text = extract_text_from_pdf(uploaded_file)
    elif file_extension == "docx":
        text = extract_text_from_docx(uploaded_file)
    elif file_extension in ["jpg", "png"]:
        text = extract_text_from_image(uploaded_file)
    else:
        st.error("Unsupported file format! Please upload a PDF, DOCX, JPG, or PNG.")

    return text

# Function to predict job roles
def predict_job_roles(resume_text):
    if not resume_text:
        return [], "No text extracted"

    # Get probabilities for all job roles
    job_probs = pipeline.predict_proba([resume_text])[0]

    # Get top 3-6 job roles
    top_indices = np.argsort(job_probs)[-6:][::-1]  # Get indices of highest probabilities
    job_roles = pipeline.classes_[top_indices]  # Get corresponding job titles

    # Select the **best-suited job role** (highest probability)
    best_role = job_roles[0]

    return job_roles, best_role

# Streamlit UI
st.title("🔍 AI Resume Screening")
st.write("Upload your resume, and the AI will recommend the **best job roles** for you.")

uploaded_file = st.file_uploader("Upload Resume (PDF, DOCX, JPG, PNG)", type=["pdf", "docx", "jpg", "png"])

if uploaded_file is not None:
    st.write("📄 **Uploaded File:**", uploaded_file.name)

    # Process resume
    resume_text = process_resume(uploaded_file)

    if resume_text:
        job_recommendations, best_job_role = predict_job_roles(resume_text)

        if len(job_recommendations) > 0:  # ✅ Fixed condition
            st.subheader("✨ Recommended Job Roles")
            for job in job_recommendations:
                st.write(f"- {job}")

            st.success(f"🎯 **Best-Suited Job Role: {best_job_role}**")
        else:
            st.warning("⚠️ No job recommendations could be generated. Try another resume.")
    else:
        st.warning("⚠️ No text extracted from the resume. Please check the file and try again.")

st.write("---")
st.write("Made with ❤️ for SmartSync!")
