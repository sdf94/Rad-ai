import requests

url = "http://localhost:8000/summarize/"
data = {
"text": "This is a long text input that needs to be summarized. The FastAPI service should be able to handle lengthy inputs and generate a coherent summary based on the user-defined summary length...",
"summary_length": 50
}

response = requests.post(url, json=data)

print(response.json())