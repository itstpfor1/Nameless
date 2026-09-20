from main.brain.config import MODEL_TIER1
from main.func.call import call_llm


def is_stop_intent(text):
    prompt = f"""Determine if the user is saying goodbye or ending the conversation with the assistant.

Examples that mean YES (ending conversation):
"See you later" -> YES
"That's all for now" -> YES
"Goodbye" -> YES
"I'm done, thanks" -> YES
"Stop listening" -> YES

Examples that mean NO (continuing conversation):
"Hello Nameless" -> NO
"Good evening" -> NO
"What's 2 plus 2" -> NO
"Can you help me with something" -> NO
"That's interesting" -> NO

Now classify this statement. Respond with exactly one word: YES or NO.

Statement: "{text}"

Answer:"""

    result = call_llm(MODEL_TIER1, prompt).upper()
    return "YES" in result