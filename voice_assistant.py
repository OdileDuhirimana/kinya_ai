import sounddevice as sd
import wave
import torch
import torchaudio
from transformers import WhisperProcessor, WhisperForConditionalGeneration
from fuzzywuzzy import process
from gtts import gTTS
import os

# 1. Record audio
def record_audio(filename="rw_instruction.wav", duration=5, sample_rate=16000):
    print("🔴 Recording... Speak now!")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(recording.tobytes())
    print(f"✅ Recording saved as: {filename}")
    return filename

# 2. Load KinyaWhisper model
def load_model():
    model_path = "benax-rw/KinyaWhisper"
    processor = WhisperProcessor.from_pretrained(model_path)
    model = WhisperForConditionalGeneration.from_pretrained(model_path)
    return processor, model

# 3. Transcribe Kinyarwanda speech
def transcribe(processor, model, audio_path):
    waveform, sample_rate = torchaudio.load(audio_path)
    assert sample_rate == 16000, "Audio must be 16kHz!"
    generation_config = model.generation_config
    generation_config.forced_decoder_ids = None

    inputs = processor(waveform.squeeze().numpy(), sampling_rate=16000, return_tensors="pt")
    inputs["attention_mask"] = torch.ones_like(inputs["input_features"][:, :, 0])

    predicted_ids = model.generate(
        inputs["input_features"],
        attention_mask=inputs["attention_mask"],
        max_new_tokens=10,
        no_repeat_ngram_size=1,
        suppress_tokens=[],
        generation_config=generation_config,
    )

    transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
    print("📄 Transcription:", transcription)
    return transcription

# 4. Match question using fuzzy matching
def match_question(transcription):
    qa_pairs = {
        "amakuru yawe": "Ni meza, urakoze!",
        "witwa nde": "Nitwa robot y'umunyabwenge.",
        "umeze ute": "Meze neza cyane.",
        "urakora iki": "Ndi kumva no gusubiza.",
        "wamfasha": "Yego, nshobora kugufasha."
    }

    best_match, score = process.extractOne(transcription.lower(), qa_pairs.keys())
    print(f"🤖 Matched: {best_match} ({score}%)")
    if score >= 70:
        return qa_pairs[best_match]
    else:
        return "Mbabarira, sinabyumva neza."

# 5. Speak answer using gTTS
def speak_answer(text):
    print("🗣️ Responding:", text)
    tts = gTTS(text=text, lang='rw')
    tts.save("response.mp3")
    os.system("mpg123 response.mp3" if os.name != 'nt' else "start response.mp3")

# Main runner
if __name__ == "__main__":
    audio_file = record_audio()
    processor, model = load_model()
    transcription = transcribe(processor, model, audio_file)
    response = match_question(transcription)
    speak_answer(response)
