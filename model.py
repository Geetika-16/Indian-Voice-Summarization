import whisper

def load_whisper_model():
    return whisper.load_model("medium")

if __name__ == "__main__":
    print("Loading Whisper medium model...")
    model = load_whisper_model()
    print("Model loaded successfully!")
