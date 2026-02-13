from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')  # Lightweight, fast BERT
emb1 = model.encode("I am a final year student with a passion for AI.", convert_to_tensor=True)
emb2 = model.encode("I love AI and I am in my final year of engineering.", convert_to_tensor=True)

# Check similarity
similarity = util.pytorch_cos_sim(emb1, emb2)
print("Semantic Similarity:", similarity.item())
# Sample expected good answers for reference (can be adjusted)
ideal_responses = {
    "Tell me about yourself": " I am from London. I have an M.com degree from Oxford University. I graduated in 2018. I am working as a sales manager currently.",
    " Where are you currently working? What is your role? ": " I am currently working at a sunshine company. I am a sales manager. I manage the meetings and help my clients in their problems. I also take care about sales"
}

def analyze_transcript(transcript):
    feedback = {}

    for question, ideal_answer in ideal_responses.items():
        similarity = util.cos_sim(model.encode(transcript), model.encode(ideal_answer))[0][0].item()
        if similarity > 0.75:
            feedback[question] = "Excellent answer - well aligned"
        elif similarity > 0.5:
            feedback[question] = "Moderate answer - could be more specific"
        else:
            feedback[question] = "Weak answer - lacks clarity or relevance"
    
    return feedback

# Example test
if __name__ == "__main__":
    transcript_text = " I am from London. I have an M.com degree from Oxford University. I graduated in 2018. I am working as a sales manager currently."
    result = analyze_transcript(transcript_text)
    for q, fb in result.items():
        print(f"\nQ: {q}\nFeedback: {fb}")
