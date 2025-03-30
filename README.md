# AI-Powered Resume Analyzer

## 📌 Project Description
The **AI-Powered Resume Analyzer** is a Python-based web application that extracts and analyzes key details from resumes. It uses **Natural Language Processing (NLP)** to extract important information such as **name, email, phone number, and skills** from uploaded PDF resumes. The processed data is then stored in **MongoDB** for further use.

## 🚀 Features
- 📂 **Resume Upload**: Upload resumes in PDF format.
- 🔍 **NLP-Based Information Extraction**: Extracts Name, Email, Phone Number, and Skills using **spaCy**.
- 🗄️ **MongoDB Integration**: Stores extracted data for future reference.
- 🌐 **REST API**: Exposes an API endpoint for resume processing.
- 🔧 **Secure File Handling**: Ensures safe and structured file management.

## 🏗️ Tech Stack
- **Python** (Flask for API)
- **spaCy** (for NLP Processing)
- **MongoDB** (Database for storing resume data)
- **PyPDF2** (for extracting text from PDF files)
- **Flask** (Web Framework)

## 📥 Installation & Setup
### Prerequisites
Ensure you have **Python 3.7+** and **MongoDB** installed on your system.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Start MongoDB (If Not Running)
```bash
mongod --dbpath /path/to/database
```

### 4️⃣ Run the Flask Server
```bash
python app.py
```

## 📤 API Usage
### Upload Resume
- **Endpoint:** `/upload`
- **Method:** `POST`
- **Payload:**
  - `file`: PDF resume file

#### Example Request (Using cURL)
```bash
curl -X POST -F "file=@resume.pdf" http://127.0.0.1:5000/upload
```

#### Example Response
```json
{
  "message": "Resume processed successfully",
  "data": {
    "name": "John Doe",
    "email": "johndoe@example.com",
    "phone": "123-456-7890",
    "skills": ["Python", "Machine Learning", "Flask"]
  }
}
```

## 🔮 Future Enhancements
- 🏢 **Job Matching**: Recommend jobs based on extracted skills.
- 🤖 **AI-Based Skill Scoring**: Score resumes based on job fit.
- 📊 **Dashboard**: Interactive UI to manage resumes.

## 📝 License
This project is licensed under the **MIT License**.

## 📧 Contact
For queries, contact **[Your Name](mailto:your-email@example.com)** or visit the GitHub repository. 🚀

