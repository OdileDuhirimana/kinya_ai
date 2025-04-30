# 🔊 Kinyarwanda Voice Assistant

An AI-powered voice assistant that listens, understands, and responds in **Kinyarwanda**. Built using Hugging Face's **KinyaWhisper** ASR model, it enables real-time Kinyarwanda speech transcription and generates meaningful responses — designed for educational, cultural, and experimental use.

---

## 🚀 Features

- 🎙️ Voice recording from microphone
- 🧠 Speech-to-text using `KinyaWhisper`
- 🤝 Question understanding via `fuzzywuzzy`
- 🗣️ Response generation with `gTTS` (Text-to-Speech)
- 🔁 Extensible question-answer logic
- 🛠️ Fully customizable for Kinyarwanda speakers

---

## 🧾 Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install torchaudio transformers fuzzywuzzy gTTS sounddevice
```

> 🐧 On Linux, also install an MP3 player like:

```bash
sudo apt install mpg123
```

> 🪟 On Windows, use `start` or `playsound` for playing `.mp3` files.

---

## 📁 Project Structure

```bash
.
├── voice_assistant.py       # Record audio and transcribe audio
├── requirements.txt   # Python packages
├── README.md          # This file
└── rw-test01.mp3      # Sample test audio (if provided)
```

---

## ▶️ How It Works

1. Run `asr.py`, which will internally trigger `recording.py`
2. Your voice is recorded (default: 5 seconds)
3. The assistant uses `KinyaWhisper` to transcribe it
4. It matches your question to known Kinyarwanda phrases
5. It plays a spoken response back to you

---

## 🧠 Example Questions

| You Say (Kinyarwanda) | It Responds With               |
|-----------------------|-------------------------------|
| Amakuru yawe          | Ni meza, urakoze!             |
| Witwa nde             | Nitwa robot y'umunyabwenge.   |
| Umeze ute             | Meze neza cyane.              |
| Urakora iki           | Ndi kumva no gusubiza.        |
| Wamfasha              | Yego, nshobora kugufasha.     |

> 🛠️ Edit these in `match_question()` in your main file.

---

## 🔧 Customization Guide

- 🎤 Change how long to record by editing: `record_audio(duration=5)`
- 🧠 Add more Q&A in the fuzzy match section
- 🗣️ Replace TTS engine if needed (e.g. pyttsx3 for offline)
- 🧪 Plug into more advanced NLU/NLP for better understanding

---

## 📦 Model Credits

- 🤖 [benax-rw/KinyaWhisper](https://huggingface.co/benax-rw/KinyaWhisper)
- 🔗 Built using [Hugging Face Transformers](https://huggingface.co/transformers/)

---

## 👩🏾‍💻 Author

**Odile (Odiboo)**

> An inspiring ,organized boss lady empowering AI in African languages.

---

## 📜 License

MIT License — feel free to use, modify, or contribute.

---

## 🌍 Let’s Make Kinyarwanda Heard

> “Giving a voice to Kinyarwanda in the age of artificial intelligence.”

