"""Simple chatbot that uses ChatGPT with Postgres data."""
import os
from typing import List, Any

from .db import fetch_records


def ask_chatgpt(question: str, records: List[Any]) -> str:
    """Send question and records to ChatGPT and return the response text."""
    import openai

    openai.api_key = os.environ.get("OPENAI_API_KEY")
    context = "\n".join(str(r) for r in records)
    prompt = f"{question}\n\nContext:\n{context}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]


def handle_question(question: str, query: str) -> str:
    """Fetches records using the query and asks ChatGPT the question."""
    records = fetch_records(query)
    return ask_chatgpt(question, records)
