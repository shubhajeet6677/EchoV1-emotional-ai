import requests

url = "https://api-inference.huggingface.co/models/google/flan-t5-small"
headers = {
    "Authorization": "Bearer hf_your_real_token"
}

response = requests.get(url, headers=headers)
print("Status:", response.status_code)
print("Response:", response.text)
