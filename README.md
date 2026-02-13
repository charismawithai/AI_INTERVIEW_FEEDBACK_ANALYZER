🎤 AI Interview Feedback Analyzer
An AI-powered system that analyzes mock interview recordings and provides structured feedback on clarity, confidence, tone, and answer quality.
This project was built as part of the CareerByteCode AIML Projects Program.

📌 Project Overview
Interview recordings often go unanalyzed, and candidates miss valuable feedback.
This project solves that problem by building a virtual AI interview coach that analyzes:

🎙️ Candidate speech (Audio)
🎥 Body language (Video)
🧠 Answer quality (NLP + ML)
💬 Personalized improvement feedback

The system converts interview recordings into actionable insights.

🚀 Features
✅ Audio → Text transcription using Whisper
✅ Video body language analysis using OpenCV
✅ BERT-based semantic answer evaluation
✅ Smart AI feedback generator
✅ Streamlit web dashboard
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

🧪 How to Run This Project (Complete Setup Guide)
This repository currently contains only the Python source files.
Follow the steps below to run the full project on your system.

💻 Step 1 — Install Required Software
Before running the project, install these tools:

1️⃣ Install Python
Download Python 3.10+ from:
https://www.python.org/downloads/

During installation ✔️ check:
☑ Add Python to PATH
python --version

2️⃣ Install PostgreSQL (Very Important)
Download PostgreSQL:
https://www.postgresql.org/download/

During installation remember the password you set.
After install, open pgAdmin 4.

🗄️ Step 2 — Create Database & Table
Open pgAdmin → Query Tool and run:

Create Database
CREATE DATABASE interview_db;

Connect to interview_db and run:
CREATE TABLE interview_records (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    transcript TEXT,
    feedback TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

📁 Step 3 — Create Project Folder Structure
Since GitHub contains only .py files, create this folder structure manually:

INTERVIEW-FEEDBACK-ANALYZER/
│
├── audio_to_text.py
├── video_analysis.py
├── transcript_analysis.py
├── feedback_generator.py
├── db_handler.py
├── streamlit_app.py
├── requirements.txt
│
├── Interview_audio/
│     └── interview.wav
│
└── Interview_video/
      └── interview.mp4
Place your own interview audio/video files inside these folders or any referal from yputube source(interview audio and video sample recordings)

📦 Step 4 — Install Python Libraries
Open terminal inside project folder and run:
pip install streamlit
pip install openai-whisper
pip install opencv-python
pip install psycopg2-binary
pip install sentence-transformers
pip install torch
pip install numpy

⚙️ Step 5 — Update Database Credentials
Open db_handler.py and update:
conn = psycopg2.connect(
    host="localhost",
    database="interview_db",
    user="postgres",
    password="YOUR_POSTGRES_PASSWORD",
    port="5432"
)
Replace password with your PostgreSQL password.

▶️ Step 6 — Run the Application
Inside project folder run: streamlit run streamlit_app.py
Open browser:http://localhost:8501

🎉 How to Use the App
1️⃣ Upload interview audio (.wav)
2️⃣ Upload interview video (.mp4)
3️⃣ Click Analyze
4️⃣ View AI feedback
5️⃣ Enter candidate name → Save to Database - You can deploy this app by uploading into your github and it gives direct link (you can use this link anytime or share to your friends,linkedin ,If u want to create an app you can upgrade this project by applying html, css , node.js)

⚠️ Important Notes
• First run may take time (Whisper model download)
• Ensure PostgreSQL is running before launching app
• Works best with clear English interview recordings
