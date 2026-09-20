from main.input.stt import record_audio, transcribe
from main.output.tts import speak
from main.mode import classify_complexity, choose_model
from main.brain.parameters import generate_response
from main.func.fold import is_stop_intent
from main.brain.config import ASSISTANT_NAME


if __name__ == "__main__":
    print(f"{ASSISTANT_NAME} is online. Press Ctrl+C to stop.\n")
    while True:
        audio = record_audio()
        text = transcribe(audio)

        if not text.strip():
            continue

        print(f"You: {text}")

        complexity = classify_complexity(text)
        model = choose_model(complexity)
        reply = generate_response(text, model)

        print(f"[{complexity}] {ASSISTANT_NAME}: {reply}\n")
        speak(reply)

        if is_stop_intent(text):
            print(f"{ASSISTANT_NAME} has stopped.")
            break