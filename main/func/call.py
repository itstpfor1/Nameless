import requests
from main.brain.config import OLLAMA_URL


def call_llm(model, prompt):
    """Generic call to Ollama. Takes a model name and prompt, returns raw text output."""
    response = requests.post(OLLAMA_URL, json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })
    return response.json()["response"].strip()