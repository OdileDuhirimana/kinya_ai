
# 🔊 Kinyarwanda Voice Assistant

An AI-powered voice assistant that listens, understands, and responds in **Kinyarwanda**. Built using Hugging Face's **KinyaWhisper** ASR model, it enables real-time Kinyarwanda speech transcription and generates meaningful responses — designed for educational, cultural, and experimental use.

---

## 🚀 Features

- 🎙️ Real-time voice recording from your microphone
- 🧠 Kinyarwanda speech-to-text transcription using `KinyaWhisper`
- 🔍 Question matching via fuzzy logic (`fuzzywuzzy`)
- 🗣️ Spoken responses using `gTTS` (Google Text-to-Speech)
- ⚙️ Fully customizable Q&A logic for conversational design

---

## 🧾 Requirements

Install all required dependencies:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install torch torchaudio transformers fuzzywuzzy python-Levenshtein gTTS sounddevice
```

> 🐧 **Linux users**: Install `mpg123` to play MP3 audio:
```bash
sudo apt install mpg123
```

> 🪟 **Windows users**: Uses the default media player via `start`.

---

## 📁 Project Structure

```bash
.
├── voice_assistant.py       # Main assistant logic (record, transcribe, respond)
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation (this file)
└── rw_instruction.wav       # Temporary audio file (created at runtime)
```

---

## ▶️ How It Works

1. Run the Python script:
   ```bash
   python voice_assistant.py
   ```

2. It records your voice for 5 seconds  
3. Transcribes Kinyarwanda speech using `KinyaWhisper`  
4. Finds a matching question using fuzzy logic  
5. Speaks the answer back in Kinyarwanda

---

## 🧠 Sample Questions

| You Say (Kinyarwanda) | It Responds With               |
|-----------------------|-------------------------------|
| Amakuru yawe          | Ni meza, urakoze!             |
| Witwa nde             | Nitwa robot y'umunyabwenge.   |
| Umeze ute             | Meze neza cyane.              |
| Urakora iki           | Ndi kumva no gusubiza.        |
| Wamfasha              | Yego, nshobora kugufasha.     |
| Nitwa nde             | Izina yawe ni Odile.          |

> 🛠️ You can modify these in the `match_question()` function.

---

## 🔧 Customization Guide

- ⏱️ Adjust recording time in `record_audio(duration=5)`
- ➕ Add or update questions in `qa_pairs` dictionary
- 🗣️ Swap `gTTS` for offline TTS like `pyttsx3` if needed
- 📈 Extend NLP with better intent detection if expanding

---

## 📦 Model Credits

- 🤖 Model: [benax-rw/KinyaWhisper](https://huggingface.co/benax-rw/KinyaWhisper)
- 🔗 Framework: [Hugging Face Transformers](https://huggingface.co/transformers/)

---

## 👩🏾‍💻 Author

**Odile (a.k.a. Odiboo)**

> An organized, inspiring boss lady shaping AI for African languages and education.

---

## 📜 License

**MIT License** — Free to use, modify, and distribute.

