from agent.knowledge_base import get_vectorstore
from agent.persona import detect_persona
from agent.search_utils import should_search_web, search_web
import os
import requests

vectorstore = get_vectorstore()
retriever = vectorstore.as_retriever()

def summarize_with_openrouter(text):
    import os
    import requests

    api_key = os.getenv("OPENROUTER_API_KEY")
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "mistralai/mistral-7b-instruct",  # Economic, fast, OpenRouter-compatible
        "messages": [
            {
                "role": "user",
                "content": f"Please summarize this Bangalore guide text in 4 lines, tailored for a tourist:\n\n{text}"
            }
        ],
        "max_tokens": 250,
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[Summarization failed] {e}"



def get_response(query, chat_history):
    persona = detect_persona(query)
    parts = []

    # If query needs real-time info
    if should_search_web(query):
        web_info = search_web(query)
        parts.append(f"📡 Current Info: {web_info}")
    
    # Get relevant chunk from vectorstore
    docs = retriever.get_relevant_documents(query)
    if docs:
        raw_chunk = docs[0].page_content.strip()
        summary = summarize_with_openrouter(raw_chunk)
    else:
        summary = "Sorry, I couldn’t find any info about that in the PDF."

    # Add persona-based prefix
    if persona == "tourist":
        parts.append(f"🌆 Tourist Tip: {summary}")
    elif persona == "resident":
        parts.append(f"🏡 Local Advice: {summary}")
    else:
        parts.append(summary)

    return "\n\n".join(parts), persona
