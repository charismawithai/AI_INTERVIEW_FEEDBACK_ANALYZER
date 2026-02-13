🎤 AI Interview Feedback Analyzer

An AI-powered virtual interview coach that analyzes mock interview recordings and generates structured feedback on clarity, confidence, tone, and answer quality.

This project was developed as part of the CareerByteCode AIML Projects Program.

📌 Project Overview

Interview recordings often go unanalyzed, and candidates miss valuable insights about their performance.

This project solves that problem by building a Virtual AI Interview Coach that analyzes:

🎙️ Candidate Speech (Audio)

🎥 Body Language (Video)

🧠 Answer Quality (NLP + ML)

💬 Personalized Improvement Feedback

The system converts interview recordings into actionable AI insights.

🚀 Features

✅ Audio → Text transcription using Whisper

✅ Video body language analysis using OpenCV

✅ BERT-based semantic answer evaluation

✅ Smart AI feedback generator

✅ Streamlit interactive web dashboard

✅ PostgreSQL database storage

🧠 Tech Stack
| Area               | Tools Used                   |
| ------------------ | ---------------------------- |
| Programming        | Python                       |
| Speech Recognition | OpenAI Whisper               |
| NLP & ML           | Sentence Transformers (BERT) |
| Computer Vision    | OpenCV                       |
| Frontend           | Streamlit                    |
| Database           | PostgreSQL                   |
| Backend            | Psycopg2                     |





🏗️ System Architecture

Interview Audio (.wav) → Whisper → Transcript

Interview Video (.mp4) → OpenCV → Body Language Insights

                ↓
Transcript Analysis → BERT Semantic Similarity

                ↓
Smart Feedback Generator (Rule-based NLP)

                ↓
Streamlit Dashboard → PostgreSQL Database


📂 Project Files

audio_to_text.py          → Whisper transcription

video_analysis.py         → OpenCV face detection

transcript_analysis.py    → BERT similarity analysis

feedback_generator.py     → Smart AI feedback engine

db_handler.py             → PostgreSQL integration

streamlit_app.py          → Streamlit web app

🧪 How to Run This Project

This repository contains only Python source files.
Follow the steps below to run the complete project.

💻 Step 1 — Install Required Software
Install Python (3.10+)

Download from:
👉 https://www.python.org/downloads/

During installation enable: ✔ Add Python to PATH

Verify installation: python --version

Install PostgreSQL

Download PostgreSQL:
👉 https://www.postgresql.org/download/

After installation open pgAdmin 4.


🗄️ Step 2 — Create Database & Table

Open pgAdmin → Query Tool → Run:

Create Database
CREATE DATABASE interview_db;

Create Table
CREATE TABLE interview_records (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    transcript TEXT,
    feedback TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

📁 Step 3 — Create Folder Structure

Since GitHub has only .py files, create this manually:


INTERVIEW-FEEDBACK-ANALYZER/

│
├── audio_to_text.py

├── video_analysis.py

├── transcript_analysis.py

├── feedback_generator.py

├── db_handler.py

├── streamlit_app.py

│
├── Interview_audio/
      └── interview.wav
│
└── Interview_video/
      └── interview.mp4



Add your own interview audio/video files.

📦 Step 4 — Install Libraries

Open terminal in project folder:

pip install streamlit
pip install openai-whisper
pip install opencv-python
pip install psycopg2-binary
pip install sentence-transformers
pip install torch numpy

⚙️ Step 5 — Update Database Credentials

Open db_handler.py and update:

conn = psycopg2.connect(
    host="localhost",
    database="interview_db",
    user="postgres",
    password="YOUR_PASSWORD",
    port="5432"
)

▶️ Step 6 — Run Application
streamlit run streamlit_app.py


Open browser:

http://localhost:8501

🎉 How to Use

1️⃣ Upload interview audio (.wav)
2️⃣ Upload interview video (.mp4)
3️⃣ Click Analyze
4️⃣ View AI feedback
5️⃣ Enter candidate name → Save to database

🎯 Learning Outcomes

Built an end-to-end AI application

Integrated NLP + Computer Vision

Developed Streamlit production app

Implemented PostgreSQL database

Gained real-world project experience

👩‍💻 Author

Charishma Devi
AI/ML Enthusiast | Python Developer

Project completed under CareerByteCode AIML Program

⭐ If you like this project, consider giving it a star!
