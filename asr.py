from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torch
import torchaudio
from fuzzywuzzy import process

# Load model (KinyaWhisper)
model_path = "benax-rw/KinyaWhisper"
processor = WhisperProcessor.from_pretrained(model_path)
model = WhisperForConditionalGeneration.from_pretrained(model_path)

# Load and validate audio
waveform, sample_rate = torchaudio.load(r"/home/odiboo/Documents/Y3/Academics/Projects/AI/Kinyarwanda/rw-test01.mp3")
assert sample_rate == 16000, "Audio must be 16kHz!"
generation_config = model.generation_config
generation_config.forced_decoder_ids = None

# Process inputs with attention mask
inputs = processor(waveform.squeeze().numpy(), sampling_rate=16000, return_tensors="pt")
inputs["attention_mask"] = torch.ones_like(inputs["input_features"][:, :, 0])

# Generate with safeguards
predicted_ids = model.generate(
    inputs["input_features"],
    attention_mask=inputs["attention_mask"],
    max_new_tokens=5,  # Strict length limit
    no_repeat_ngram_size=1,
    suppress_tokens=[],  # Disable token blocking
    generation_config=generation_config,
)

# Decode
transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
print("Output:", transcription)