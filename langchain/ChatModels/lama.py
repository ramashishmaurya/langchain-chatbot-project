import requests

response = requests.post(
    "http:// localhost:11434/api/generate",
    json={
        "model": "llama3",
        "prompt": "Explain Python in simple words",
        "stream": False
    }  
)

print(response.json()["response"])
