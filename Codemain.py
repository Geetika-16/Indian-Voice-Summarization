import sys
sys.stdout.reconfigure(encoding='utf-8')
from llama_cpp import Llama
import sounddevice as sd
import wavio
from model import load_whisper_model
import os
from deep_translator import GoogleTranslator


audio_file = "audio.wav"

# ---- LOAD LLaMA MODEL ----
llm = Llama(
    model_path="model\llama-2-7b-chat.Q4_K_M.gguf",
    n_ctx=2048
)

# ------------------ INITIALIZATION ------------------

print("==============================================")
print(" Indian Regional Language Voice Summarization ")
print(" Supports Tamil, Hindi, Telugu, English etc. ")
print("==============================================\n")

# ------------------ WELCOME --------------------
print("Welcome to the Indian Voice Summarization")

# ------------------ VOICE INPUT ------------------
duration = 5  
fs = 44100    # sample rate
print("Listening...")

recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()  
audio_file = "audio.wav"
wavio.write(audio_file, recording, fs, sampwidth=2)


# ------------------ SPEECH TO TEXT ------------------
print("Processing audio...")
try:
    model = load_whisper_model()  

    result = model.transcribe(audio_file)  
    detected_lang =result['language']
    text = result['text'].strip()

    print(f"\nDetected Language Code: {detected_lang}")
    print(f"Original Text:\n {text}")
    
    with open("transcription.txt", "w", encoding="utf-8") as f:
        f.write(text)
    
    print("\nTranscription saved to transcription.txt")
except Exception as e:
    print("Sorry, could not recognize speech.")
    print("Error:", e)
    exit()

# ------------------ INDIAN LANGUAGE FILTER ------------------

INDIAN_LANGS = [
    "as","bn","brx","doi","gu","hi","kn","ks","kok","mai",
    "ml","mr","mni","ne","or","pa","sa","sat","sd","ta","te","ur"
]

if detected_lang not in INDIAN_LANGS:
    print("Non-Indian language detected.") #Forcing Indian Languages

    for lang in INDIAN_LANGS:
        retry = model.transcribe(audio_file, language=lang)
        retry_text = retry["text"].strip()

        if len(retry_text) > 5:
            detected_lang = lang
            text = retry_text
            print("Corrected Language:", detected_lang)
            print("Corrected Text:", text)
            break

# ------------------ LANGUAGE DETECTION ------------------

detected_lang = result['language']
print("\nDetected Language Code:", detected_lang)

# ------------------ TRANSLATE TO ENGLISH  ------------------

if detected_lang != "en":
    english_text = GoogleTranslator(source=detected_lang, target="en").translate(text)
else:
    english_text = text
print("\nTranslated Text (English):")
print("English Text:",english_text)

# ------------------ SUMMARIZATION ------------------

prompt = f"""
Summarize the following text in a clear and concise manner:

{english_text}
"""

response = llm(
    prompt,
    max_tokens=300,
    temperature=0.4
)

english_summary = response["choices"][0]["text"].strip()

print("\n--- English Summary ---")
print(english_summary)

# ------------------ OPTIONAL TRANSLATION ------------------

choice = input("\nDo you want the summary in another language? (yes/no): ").lower()

if choice == "yes":
    target_lang = input("Enter language name: ")
    translated_summary = GoogleTranslator(
        source="en", target=target_lang
    ).translate(english_summary)

    print("\n--- Translated Summary ---")
    print(translated_summary)

# ------------------ EXIT ------------------

print("\nThank you for using Indian Voice Summarization System.")
