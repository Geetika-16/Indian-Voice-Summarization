# Indian Regional Language Voice Summarization using LLM

This project is a voice-based multilingual summarization system that converts spoken input from Indian regional languages into concise summaries using modern AI models. The system records a user's voice, converts speech to text, translates it to English, generates a summary using a local Large Language Model, and optionally translates the summary back to another language.

The project demonstrates the integration of speech recognition, language detection, machine translation, and large language models into a complete AI pipeline.

The summarization component is powered by a locally running LLaMA model through llama.cpp, while speech recognition is performed using Whisper.

# Features

• Voice recording using microphone input
• Speech-to-text conversion using Whisper
• Automatic language detection
• Support for multiple Indian regional languages including Tamil, Hindi, Telugu, Malayalam, Kannada, Marathi and others
• Translation to English for processing
• Text summarization using a local LLaMA model
• Optional translation of summary into another language
• Fully offline LLM summarization (no paid APIs)

# Supported Languages

The system is designed to handle many Indian languages such as:
Tamil
Hindi
Telugu
Malayalam
Kannada
Marathi
Bengali
Punjabi
Gujarati
and several other Indian regional languages.

# Technologies Used

Python 3.10 version
Speech Recognition and Audio Processing
Whisper Speech-to-Text Model
Local LLM using llama.cpp
Translation using Deep Translator
Audio Recording with sounddevice and wavio


# Project Goal

The goal of this project is to demonstrate how multilingual speech processing and large language models can be combined to build intelligent AI systems capable of understanding and summarizing spoken content from diverse Indian languages.

# Future Improvements

• Web interface using Flask or Gradio
• Real-time streaming speech input
• Speaker diarization
• More accurate multilingual translation
• Deployment as an online AI service
