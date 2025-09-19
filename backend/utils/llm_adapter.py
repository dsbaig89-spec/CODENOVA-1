# llm_adapter.py
import os
import requests

LLM_API_URL = os.getenv("LLM_API_URL")
LLM_API_KEY = os.getenv("LLM_API_KEY")

def generate_reply(system_prompt: str, user_text: str):
    if not LLM_API_URL or not LLM_API_KEY:
        raise RuntimeError("LLM not configured")
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_text}
        ],
        "temperature": 0.2
    }
    headers = {"Authorization": f"Bearer {LLM_API_KEY}", "Content-Type": "application/json"}
    resp = requests.post(LLM_API_URL, json=payload, headers=headers, timeout=20)
    resp.raise_for_status()
    data = resp.json()
    return data.get("choices", [{}])[0].get("message", {}).get("content", "")
