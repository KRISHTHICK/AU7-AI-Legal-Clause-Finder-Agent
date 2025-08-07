# AU7-AI-Legal-Clause-Finder-Agent
Ai Agent

AI Legal Clause Finder Agent
🧠 Description:
This AI agent helps users extract and understand legal clauses from contracts or legal documents (in .txt or .docx format). Users can upload a file and ask questions like "What is the termination clause?" or "What are the confidentiality terms?", and the agent answers based on the document content.

🛠️ Stack:
Python

Streamlit (UI)

LangChain or custom prompt logic

Ollama / Local LLM (e.g., TinyLLaMA or Mistral)

docx2txt, PyMuPDF, dotenv

✅ Features:
Upload .docx or .pdf

Extract text from documents

Ask natural questions about clauses

Local LLM-based QA

Predefined buttons for key clauses (Termination, Confidentiality, Jurisdiction, etc.)

🏁 To Run the App:
bash
Copy
Edit
pip install -r requirements.txt
streamlit run app.py
