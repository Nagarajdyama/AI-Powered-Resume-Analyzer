import os
import re
import json
import pymongo
import PyPDF2
import spacy
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename

# Load NLP Model
nlp = spacy.load("en_core_web_sm")

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["ResumeDB"]
collection = db["resumes"]

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Extract Text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

# Extract Information from Resume
def extract_info(text):
    doc = nlp(text)
    info = {
        "name": None,
        "email": None,
        "phone": None,
        "skills": [],
    }
    
    # Extract Email
    email_match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    if email_match:
        info["email"] = email_match.group(0)
    
    # Extract Phone Number
    phone_match = re.search(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", text)
    if phone_match:
        info["phone"] = phone_match.group(0)
    
    # Extract Name (First Named Entity)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            info["name"] = ent.text
            break
    
    # Extract Skills (Basic Keyword Matching)
    skills_list = ["Python", "Java", "Machine Learning", "AI", "Data Science", "Flask", "MongoDB"]
    for token in doc:
        if token.text in skills_list:
            info["skills"].append(token.text)
    
    return info

# Resume Upload and Analysis
@app.route("/upload", methods=["POST"])
def upload_resume():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400
    
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)
    
    # Extract text and analyze
    text = extract_text_from_pdf(filepath)
    extracted_info = extract_info(text)
    
    # Store in MongoDB
    collection.insert_one(extracted_info)
    
    return jsonify({"message": "Resume processed successfully", "data": extracted_info})

if __name__ == "__main__":
    app.run(debug=True)
