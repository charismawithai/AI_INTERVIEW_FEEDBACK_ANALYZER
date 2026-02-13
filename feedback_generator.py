def generate_feedback(transcript, video_insights):
    transcript_lower = transcript.lower()
    insights_lower = video_insights.lower()

    feedback = "<div style='font-size:16px; line-height:1.8'>"
    feedback += "🧠 <b>AI Interview Coach Feedback:</b><br><br>"

    # 🔹 Clarity
    if any(word in transcript_lower for word in ["uh", "um", "like", "you know", "i guess"]):
        feedback += "🔹 <b>Clarity:</b> The candidate's response included filler words that slightly disrupted the flow. Practicing with structured answers could improve clarity.<br><br>"
    else:
        feedback += "🔹 <b>Clarity:</b> The candidate communicated ideas clearly with minimal hesitation or verbal fillers.<br><br>"

    # 🔹 Confidence
    if "nervous" in insights_lower:
        feedback += "🔹 <b>Confidence:</b> While maintaining eye contact was good, signs of nervousness were noticeable. With more practice, the candidate can boost confidence and reduce hesitation.<br><br>"
    elif "confident" in insights_lower:
        feedback += "🔹 <b>Confidence:</b> The candidate appeared confident and self-assured, which positively impacted their delivery.<br><br>"
    else:
        feedback += "🔹 <b>Confidence:</b> The candidate showed moderate confidence. Pauses and steady speech can enhance delivery.<br><br>"

    # 🔹 Tone
    if "calm" in insights_lower:
        feedback += "🔹 <b>Tone:</b> The tone was calm and professional, contributing to a positive impression.<br><br>"
    elif "monotone" in insights_lower:
        feedback += "🔹 <b>Tone:</b> The tone lacked variation, which may make answers feel flat. Use emphasis to show enthusiasm.<br><br>"
    elif "energetic" in insights_lower:
        feedback += "🔹 <b>Tone:</b> The tone was engaging and reflected strong enthusiasm.<br><br>"
    else:
        feedback += "🔹 <b>Tone:</b> The tone was neutral and acceptable, but can be improved with more vocal variation.<br><br>"

    # 🔹 Answer Quality
    if any(word in transcript_lower for word in ["project", "experience", "problem", "solution", "internship", "achievement"]):
        feedback += "🔹 <b>Answer Quality:</b> The response demonstrated a solid understanding with real-world examples, making it strong and convincing.<br><br>"
    else:
        feedback += "🔹 <b>Answer Quality:</b> The answer lacked specific examples. Mentioning projects, outcomes, or achievements could make it more impactful.<br><br>"

    # ✅ Summary
    feedback += "✅ <b>Summary:</b> With slight improvements in tone and confidence, the candidate has the potential to deliver highly effective and professional interviews."

    feedback += "</div>"
    return feedback

# Optional test
if __name__ == "__main__":
    transcript = "Good morning. I am Simon..."
    video_insights = "Candidate maintained eye contact and spoke in a calm tone, but showed signs of nervousness during answers. Average body language"
    print(generate_feedback(transcript, video_insights))
