import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # ✅ Secure way to use API key

def ask_ai(query):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": query}]
    )
    return response["choices"][0]["message"]["content"]