from main.brain.config import MODEL_TIER1, MODEL_TIER2
from main.func.call import call_llm

def classify_complexity(text):
    prompt = f"""Classify the following user request as either SIMPLE or COMPLEX.
SIMPLE = greetings, basic facts, direct simple commands, short factual questions.
COMPLEX = multi-step reasoning, analysis, game-state tracking, planning, anything requiring real thought.

Request: "{text}"

Respond with exactly one word: SIMPLE or COMPLEX."""

    result = call_llm(MODEL_TIER1, prompt).upper()
    return "COMPLEX" if "COMPLEX" in result else "SIMPLE"


def choose_model(complexity):
    """Maps a complexity level to the model that should handle it.
    Today: binary. Later: expand to a 0-10 scale mapping to more tiers."""
    return MODEL_TIER1 if complexity == "SIMPLE" else MODEL_TIER2