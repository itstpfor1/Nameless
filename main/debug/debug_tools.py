from main.brain.config import DEBUG_MODE

def debug_print(label, value):
    if DEBUG_MODE:
        print(f"[DEBUG {label}]: {value}")