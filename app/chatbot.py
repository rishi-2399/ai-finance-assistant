import openai


def ask_ai(query):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": query}],
    )
    return response["choices"][0]["message"]["content"]
