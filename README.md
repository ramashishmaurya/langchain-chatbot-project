# 🦜 LangChain Chatbot Project

A hands-on learning project built while exploring **LangChain** from scratch — covering chains, prompts, memory, agents, tools, and Streamlit UI.

---

## 🎯 What I Built & Learned

```
LangChain Basics
      ↓
ChatPromptTemplate + Chains
      ↓
Memory (conversation history)
      ↓
Tools + Agents
      ↓
Streamlit UI
      ↓
Ollama (local LLM) integration
```

---

## ⚙️ Tech Stack

| Tool | Purpose |
|------|---------|
| **LangChain 0.3.7** | LLM orchestration framework |
| **Ollama** | Local LLM (llama3) — free, private |
| **Streamlit** | Frontend UI |
| **ChatPromptTemplate** | Structured prompt building |
| **Session State** | Conversation memory |
| **Python-dotenv** | Environment variables |

---

## 🧠 LangChain Concepts Covered

### 1. Basic Chain — Pipe Operator
```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

llm    = ChatOllama(model="llama3")
prompt = ChatPromptTemplate.from_template("Tell me about {topic}")

# Pipe operator — LangChain ka magic!
chain    = prompt | llm
response = chain.invoke({"topic": "Python"})
print(response.content)
```

### 2. Memory — Conversation History
```python
from langchain_core.messages import HumanMessage, AIMessage

chat_history = []

def chat(user_input):
    chat_history.append(HumanMessage(content=user_input))
    response = llm.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    return response.content

# Context yaad rehta hai!
chat("Mera naam Ramashish hai")
chat("Mera naam kya hai?")  # → "Ramashish" ✅
```

### 3. Streaming — Real Time Response
```python
# Piece by piece response — ChatGPT jaisa!
for chunk in chain.stream({"topic": "AI"}):
    print(chunk.content, end="", flush=True)
```

### 4. Tools + Agent
```python
from langchain.tools import tool

@tool
def calculator(expression: str) -> str:
    """Math calculate karo"""
    return str(eval(expression))

# Agent khud decide karta hai kaunsa tool use karna hai!
```

### 5. Streamlit Session State
```python
# Page reload ke baad bhi memory rehti hai!
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
```

---

## 🚀 Quick Start

### Step 1 — Clone
```bash
git clone https://github.com/ramashishmaurya/langchain-chatbot-project.git
cd langchain-chatbot-project
```

### Step 2 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Setup Ollama
```bash
# ollama.com se install karo
ollama pull llama3
ollama serve
```

### Step 4 — Environment setup
```bash
# .env file banao (langchain/ folder mein)
# OPENAI_API_KEY=your_key_here  
# GROQ_API_KEY=your_key_here    
```

### Step 5 — Run
```bash
# Streamlit app
streamlit run app/app.py

# Ya individual scripts
python langchain/chains.py
python langchain/memory.py
```

---

## 🔄 LangChain Version Used

```txt
langchain==0.3.7
langchain-core==0.3.15
langchain-community==0.3.7
langchain-ollama==0.2.1
streamlit>=1.31.0
python-dotenv==1.0.0
pydantic==2.9.2
```

---

## 💡 Key Learnings

```
✅ Pipe operator (prompt | llm) — chain banana
✅ ChatPromptTemplate — structured prompts
✅ Streaming — real time text output
✅ HumanMessage / AIMessage — chat history
✅ Session state — Streamlit memory
✅ @tool decorator — custom tools banana
✅ Separate files — modular project structure
✅ .gitignore — API keys safe rakhna
✅ Ollama — local LLM, free aur private
```

---

## ⚠️ Important — API Key Safety

```bash
# .gitignore mein yeh hona chahiye:
.env
**/.env
langchain/.env

# .env.example banao (actual key nahi):
OPENAI_API_KEY=your_key_here
GROQ_API_KEY=your_key_here
```

---

## 🔮 Next Steps

- [ ] RAG pipeline — PDF chatbot
- [ ] LangGraph — agentic workflows  
- [ ] ChromaDB — vector database
- [ ] LangSmith — experiment tracking
- [ ] Deploy on Streamlit Cloud

---

## 📚 Resources

- [LangChain Docs](https://python.langchain.com/docs)
- [Ollama](https://ollama.com)
- [Groq (free API)](https://groq.com)
- [LangGraph](https://langchain-ai.github.io/langgraph)

---

## 👤 Author

**Ramashish Maurya**
GitHub: [@ramashishmaurya](https://github.com/ramashishmaurya)
