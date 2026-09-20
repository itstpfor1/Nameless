import wave
import io
import numpy as np
import sounddevice as sd
from piper import PiperVoice
from main.brain.config import VOICE_MODEL_PATH

voice = PiperVoice.load(VOICE_MODEL_PATH)


def speak(text):
    buffer = io.BytesIO()

    with wave.open(buffer, 'wb') as wav_file:
        voice.synthesize_wav(text, wav_file)

    buffer.seek(0)
    with wave.open(buffer, 'rb') as wav_file:
        frames = wav_file.readframes(wav_file.getnframes())
        sample_rate = wav_file.getframerate()
        audio_array = np.frombuffer(frames, dtype=np.int16)

    sd.play(audio_array, samplerate=sample_rate)
    sd.wait()