import whisper
import warnings

# Suppress UserWarnings
warnings.filterwarnings("ignore", category=UserWarning)

def transcribe_with_whisper(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path, language='en')
    return result['text']

if __name__ == "__main__":
    audio_path = r"C:\Users\polot\OneDrive\Desktop\interview-feedback-analyzer\Interview_audio\interview2.wav"

    text = transcribe_with_whisper(audio_path)
    print("📝 Whisper Transcript:\n", text)
