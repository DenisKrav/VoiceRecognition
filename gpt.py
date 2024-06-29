import os

from groq import Groq

client = Groq(
    api_key="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",
)

def generate(prompt):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama3-8b-8192",
    )

    return chat_completion.choices[0].message.content