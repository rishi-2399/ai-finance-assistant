import openai

OPENAI_API_KEY = "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"

def ask_ai(query):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": query}],
        api_key=OPENAI_API_KEY
    )
    return response["choices"][0]["message"]["content"]
