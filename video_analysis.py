import cv2

def analyze_video(video_path):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(video_path)

    expression_count = 0
    total_frames = 0
    frame_skip = 10  # Analyze every 10th frame

    frame_index = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if frame_index % frame_skip == 0:
            total_frames += 1
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            if len(faces) > 0:
                expression_count += 1

        frame_index += 1

    cap.release()
    cv2.destroyAllWindows()

    if total_frames == 0:
        return "No valid frames to analyze."

    face_ratio = expression_count / total_frames
    if face_ratio > 0.7:
        return "Good eye contact and facial visibility"
    elif face_ratio > 0.3:
        return "Average body language"
    else:
        return "Poor visibility or no expressions"

# Test
if __name__ == "__main__":
    feedback = analyze_video("C:/Users/polot/OneDrive/Desktop/interview-feedback-analyzer/interview1 (2).mp4")
    print("Body Language Feedback:", feedback)
