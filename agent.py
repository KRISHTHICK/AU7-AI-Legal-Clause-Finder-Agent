import subprocess
import os
from prompt_template import build_prompt

def run_ollama_query(prompt, model="tinyllama"):
    """Runs the prompt using Ollama's API via subprocess"""
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.stdout.decode("utf-8")
