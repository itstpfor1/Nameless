import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel
from main.brain.config import SAMPLE_RATE, SILENCE_THRESHOLD, SILENCE_DURATION

model = WhisperModel("base", device="cpu", compute_type="int8")


def record_audio():
    print("🎤 Listening...")
    chunks = []
    silence_time = 0.0
    speech_started = False
    chunk_duration = 0.1
    chunk_samples = int(SAMPLE_RATE * chunk_duration)

    with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype='float32') as stream:
        while True:
            chunk, _ = stream.read(chunk_samples)
            volume = np.abs(chunk).mean()
            chunks.append(chunk)

            if volume > SILENCE_THRESHOLD:
                speech_started = True
                silence_time = 0.0
            elif speech_started:
                silence_time += chunk_duration

            if speech_started and silence_time >= SILENCE_DURATION:
                break

    audio = np.concatenate(chunks).flatten()
    return audio


def transcribe(audio):
    segments, _ = model.transcribe(audio, language="en")
    return " ".join(segment.text for segment in segments).strip()