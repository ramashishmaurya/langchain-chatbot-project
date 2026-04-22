import ollama

response = ollama.chat(
    model='llama3',
    messages=[
        {"role": "user", "content": "what is human"}
    ]
)

print(response['message']['content'])