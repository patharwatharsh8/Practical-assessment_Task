from datetime import datetime
from config import settings

def write_output(question, answer):
    with open(settings.OUTPUT_FILE, "a") as f:
        f.write(f"\n[{datetime.now()}]\n")
        f.write(f"Q: {question}\n")
        f.write(f"A: {answer}\n")
