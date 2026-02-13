import streamlit as st
from audio_to_text import transcribe_with_whisper
from video_analysis import analyze_video
from transcript_analysis import analyze_transcript
from feedback_generator import generate_feedback
from db_handler import save_record
import tempfile
import re  # ✅ for removing HTML tags

# 🖥️ Page config
st.set_page_config(page_title="Interview Feedback Analyzer", layout="wide")

# 🧼 CSS styling
st.markdown("""
    <style>
        .main {
            max-width: 1200px;
            padding: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# 🎯 Title
st.title("🎤 AI-based Interview Feedback Analyzer")

# 📤 Upload section
audio_file = st.file_uploader("Upload Interview Audio (.wav)", type=["wav"])
video_file = st.file_uploader("Upload Interview Video (.mp4)", type=["mp4"])

# ⏳ Session state init
if 'transcript' not in st.session_state:
    st.session_state.transcript = None
if 'final_feedback' not in st.session_state:
    st.session_state.final_feedback = None

# ▶️ Analyze section
if st.button("Analyze"):
    if audio_file and video_file:
        # 1️⃣ Audio transcription
        st.subheader("1️⃣ Transcript from Audio")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            temp_audio.write(audio_file.read())
            temp_audio_path = temp_audio.name
        transcript = transcribe_with_whisper(temp_audio_path)
        st.session_state.transcript = transcript
        st.write(transcript)

        # 2️⃣ Video analysis
        st.subheader("2️⃣ Video Body Language Insights")
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
            temp_video.write(video_file.read())
            temp_video_path = temp_video.name
        video_result = analyze_video(temp_video_path)
        st.write(video_result)

        # 3️⃣ BERT Transcript Feedback
        st.subheader("3️⃣ BERT-based Transcript Feedback")
        bert_feedback = analyze_transcript(transcript)
        for question, feedback in bert_feedback.items():
            st.markdown(f"**🗨️ {question.strip()}**\n\n🔎 _{feedback}_\n")

        # 4️⃣ AI Final Feedback
        st.subheader("4️⃣ AI Smart Feedback 💬")
        final_feedback = generate_feedback(transcript, video_result)
        st.session_state.final_feedback = final_feedback
        st.markdown(final_feedback, unsafe_allow_html=True)
    else:
        st.warning("Please upload both audio and video files.")

# 💾 Save to DB Section
st.subheader("💾 Save Feedback")
name = st.text_input("Candidate Name", "")

if st.button("Save Feedback to DB"):
    if name.strip() and st.session_state.transcript and st.session_state.final_feedback:
        try:
            # 🧽 Clean feedback: Remove HTML tags before saving
            plain_feedback = re.sub('<[^<]+?>', '', st.session_state.final_feedback)

            # 💾 Save plain feedback
            save_record(name, st.session_state.transcript, plain_feedback)
            st.success("✅ Feedback saved successfully!")
        except Exception as e:
            st.error(f"❌ Error saving feedback: {e}")
    else:
        st.warning("⚠️ Please analyze interview and enter name before saving.")
