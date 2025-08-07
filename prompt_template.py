def build_prompt(document_text, user_query):
    return f"""
You are a legal AI assistant. Read the following legal document and answer the user's question clearly and precisely.

Document:
\"\"\"
{document_text}
\"\"\"

User's Question:
{user_query}

Answer:
"""
