# 🎙️ Indian Voice Summarization System

## Description

Indian Voice Summarization System is an AI and NLP-based application that converts spoken Indian language audio into concise English summaries. The system allows users to speak in their preferred Indian language, automatically transcribes the speech into text, translates the content into English, and generates an AI-powered summary.

The project combines Speech Recognition, Natural Language Processing (NLP), Machine Translation, and Large Language Models (LLMs) to help users quickly understand the key information contained in spoken content. It supports multiple Indian languages and can be extended for longer audio recordings and additional language translations.

---

## Features

### 🎤 Voice Input

* Accepts spoken input from users.
* Configurable recording duration.
* Supports multiple Indian languages.

### 📝 Speech-to-Text Conversion

* Converts recorded speech into text.
* Generates transcription in the original spoken language.
* Powered by Whisper speech recognition.

### 🌐 Language Translation

* Translates recognized text into English.
* Supports multiple Indian languages.
* Uses automatic language mapping and translation.

### 🤖 AI-Powered Summarization

* Generates concise summaries from translated English text.
* Extracts key information from spoken content.
* Uses a Hugging Face Large Language Model (LLM).

### 🔄 Multi-Language Translation Support

* Optional translation of the generated summary into other Indian languages.
* Improves accessibility for users from different linguistic backgrounds.

### ⚙️ Flexible Configuration

* Adjustable recording duration.
* Supports different Whisper model sizes:

  * Tiny
  * Base
  * Small
  * Medium
  * Large-v3
* Allows balancing speed and accuracy.

---

## Technologies Used

### Programming Language

* Python

### Natural Language Processing (NLP)

* Hugging Face Transformers
* Large Language Models (LLMs)

### Speech Processing

* OpenAI Whisper
* Speech Recognition

### Translation

* Deep Translator
* Google Translation Services

### Python Libraries

* Transformers
* Torch
* Whisper
* Deep Translator
* NumPy

### AI & Machine Learning

* Natural Language Processing (NLP)
* Text Summarization
* Speech Recognition
* Machine Translation

---

## Project Workflow

### Step 1: Language Selection

1. System loads supported Indian language mappings.
2. User selects or speaks in a preferred Indian language.

### Step 2: Voice Recording

1. User records speech through the microphone.
2. Audio is captured for a predefined duration.
3. Recording is stored for processing.

### Step 3: Speech-to-Text Conversion

1. Recorded audio is processed using Whisper.
2. Speech is converted into text.
3. Original language transcription is generated.

### Step 4: English Translation

1. Transcribed text is translated into English.
2. English text is prepared for summarization.

### Step 5: AI Summarization

1. English text is sent to the Hugging Face LLM.
2. The model analyzes the content.
3. A concise summary is generated.

### Step 6: Optional Language Translation

1. User may choose another Indian language.
2. Generated summary is translated into the selected language.
3. Final translated summary is displayed.

### Step 7: Output Generation

1. Original speech transcription is displayed.
2. English translation is displayed.
3. AI-generated summary is displayed.
4. Optional translated summary is displayed.

---

### Files Uploaded
1. Codemain.py - Built the main theme of the project.
2. main.py - Setting up whisper for speech processing.
3. Output image - Demo Screenshot.

---

## Outcome

The system enables users to convert spoken Indian-language content into meaningful English summaries using Speech Recognition, Machine Translation, and AI-powered NLP techniques. It helps users quickly understand lengthy spoken content while supporting multilingual accessibility.
