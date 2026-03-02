# CV Question Answering Agent (Agentic Automation)

## Overview
An agentic AI system that answers questions strictly based on a CV document using RAG architecture.

## Features
- PDF CV ingestion
- FAISS vector store
- Agent-based reasoning (LangChain)
- Conversation memory
- Grounded responses
- CLI interface
- Config-driven architecture
- Logging & error handling

## Tech Stack
- Python
- LangChain
- FAISS
- OpenAI
- Pydantic

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Add your OpenAI API key in .env

3. Run:
   python main.py

## Example Questions
- What is my highest qualification?
- What projects have I worked on?
- When did I graduate?

## Anti-Hallucination Rule
If information is not present in CV:
"This information is not available in the provided CV."

---
