# 🧠 Bangalore Smart Agent

It’s an intelligent assistant that helps both **tourists** and **new residents** navigate Bangalore using a city guide PDF and real-time LLM responses.

---

## 🔧 Features

- 📄 **PDF RAG:** Answers are grounded in the _Ultimate Bangalore Guide_ PDF using vector search
- 🧍 **Persona Awareness:** Responds differently for tourists (fun & highlights) and new residents (local tips)
- 🌐 **Real-Time Web Search:** Uses OpenRouter (Mistral-7B) to retrieve or summarize live info like event timings or fees
- ✨ **LLM Summarization:** Summarizes long PDF chunks before responding, using Gemini-style OpenRouter API
- 🔐 **Secure API Handling:** API keys stored in `.env`, never exposed
- 💡 **Prompt Engineering:** Custom tone and styling per persona

---

## 🗂 Folder Structure

```
bangalore-smart-agent/
├── agent/                 # All core logic (vector store, persona, LLM wrapper)
├── conversations/        # Sample tourist/resident/persona-switch dialogs
├── pdf/                  # Place your Bangalore guide PDF here
├── main.py               # CLI entry point
├── .env.example          # Sample for OpenRouter API key
├── requirements.txt      # Dependencies
├── .gitignore            # Excludes venv, .env, pycache
└── README.md             # You are here :)
```

---

## 🚀 How to Run

### 1. Clone this repository

```bash
git clone https://github.com/Ingenium9/bangalore-smart-agent
cd bangalore-smart-agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your API Key

Create a `.env` file in the root folder:

```env
OPENROUTER_API_KEY=your-api-key-here
```

### 4. Add the city guide PDF

Place your **“The Ultimate Bangalore Guide.pdf”** in the `pdf/` folder.

### 5. Run the Agent

```bash
python main.py
```

Try questions like:

- `I’m visiting Bangalore for the weekend. What should I see?`
- `I’m relocating to Whitefield. Where should I live?`
- `What’s the entry fee for Lalbagh right now?`

---

## 💡 Example Output

```text
User: I’m in Bangalore for a weekend. What should I definitely visit?

Agent (tourist): 🌆 Tourist Tip: Start with Lalbagh Botanical Garden and Cubbon Park. Explore Bangalore Palace and enjoy street food at VV Puram. Don’t miss Church Street’s nightlife! 🚇 Use the Purple Line for easy access.
```

---

## 🧠 Technical Stack

| Component    | Tool                                 |
| ------------ | ------------------------------------ |
| Vector DB    | FAISS via LangChain                  |
| Embeddings   | HuggingFace (MiniLM-L6-v2)           |
| LLM          | OpenRouter API (Mistral-7B Instruct) |
| Prompt Logic | Custom tone + styling per persona    |
| Interface    | CLI (Terminal-based chat)            |

---

## 📌 Notes

- `.env` is excluded via `.gitignore`
- Real-time summarization triggered only for long answers
- All vector queries are handled locally using HuggingFace embeddings
- OpenRouter API is used only when needed (cost-efficient)
