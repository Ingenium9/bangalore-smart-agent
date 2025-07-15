import os
import requests

def should_search_web(query):
    keywords = ["current", "today", "now", "latest", "fee", "entry", "price", "event", "timing", "schedule"]
    return any(word in query.lower() for word in keywords)

def search_web(query):
    api_key = os.getenv("OPENROUTER_API_KEY")
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    body = {
        "model": "google/gemini-pro",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant providing real-time, current information about Bangalore city."},
            {"role": "user", "content": query}
        ],
        "max_tokens": 300
    }

    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        data = response.json()
        return data['choices'][0]['message']['content']
    except Exception as e:
        return f"[Web search failed] {e}"
