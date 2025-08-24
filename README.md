# 🌐 Multi-Agent Language Translator 🤖💬

**Translate like a pro with AI-powered agents!**

This project is a **multi-agent AI translator system** built on **OpenAI’s Gemini models**. It orchestrates multiple specialized agents to translate text across **French, Russian, Dutch, and German** with smart fallback mechanisms for seamless results.

---

## ✨ Features

* 📝 **Multi-Language Translation:**
  Translate a single input into multiple languages effortlessly.

* 🔄 **Intelligent Handoff:**
  If one agent fails, the task is automatically passed to the next agent.

* ⚡ **Powered by OpenAI Gemini:**
  Uses `gemini-2.5-flash` for high-quality translations.

* 🔧 **Easy Setup:**
  Just add your `GEMINI_API_KEY` in `.env` and you’re ready.

* 🏃 **Synchronous Runner Support:**
  Run your main agent and get results instantly without async complexity.

---

## 💻 How It Works

1. Load environment variables with `dotenv`.
2. Initialize the OpenAI Gemini client asynchronously.
3. Define agents for French, Russian, Dutch, and German translations.
4. Create a **main agent** with fallback agents.
5. Run the main agent via `Runner.run_sync()` to get the final translation.

---

## 📦 Project Structure

```
.
├── main.py              # Run the translation
├── agents.py            # Agent & Runner definitions
├── .env                 # GEMINI_API_KEY
├── requirements.txt     # Dependencies
├── pyproject.toml       # Project metadata
└── README.md            # This file
```

---

## ⚡ Quick Start

```bash
# Clone the repository
git clone https://github.com/Ibrahim4594/Simple-OpenAI-UV-Agent.git
cd Simple-OpenAI-UV-Agent

# Add your API key
"GEMINI_API_KEY=your_api_key_here" > .env

# Run the translator
python main.py
```

---

## 🌟 Example Output

```text
Main agent translation: Hallo, ich bin Ibrahim
```

---

## 📌 Notes

* Easily **extendable**: add more agents for other languages.
* Designed for **clarity and modularity**, ideal for AI-driven multilingual applications.
* Perfect for **experiments, demos, or learning advanced AI agent orchestration**.

---

Do you want me to do that too?


