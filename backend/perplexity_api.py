import httpx
import os
from dotenv import load_dotenv
load_dotenv()


PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY")

def query_perplexity(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "sonar", 
        "messages": [
            {"role": "system", "content": "You are a music recommendation expert."},
            {"role": "user", "content": prompt}
        ]
    }

    response = httpx.post("https://api.perplexity.ai/chat/completions", headers=headers, json=payload)
    response.raise_for_status()

    return response.json()["choices"][0]["message"]["content"]
