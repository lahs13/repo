# Python Repository

This repository contains a simple Python module with a greeting function and a
minimal chatbot that uses Postgres data with ChatGPT.

## Greeting Example

```python
from src.greetings import hello
print(hello('World'))
```

## Chatbot

The chatbot fetches information from a Postgres database and forwards it to
ChatGPT. Copy `.env.example` to `.env` and adjust the values or export the
following environment variables before running:

- `DATABASE_URL` - connection string for your Postgres database
- `OPENAI_API_KEY` - API key for OpenAI

Run the chatbot handler directly:

```python
from src.chatbot import handle_question

answer = handle_question('¿Quién está en la base de datos?', 'SELECT * FROM usuarios')
print(answer)
```

## Tests

Run the unit tests with:

```bash
python -m unittest
```
