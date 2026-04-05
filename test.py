import requests

url = "http://127.0.0.1:9000/answer"
text=input("input: ")
data = {
    "text": text
}

response = requests.post(url, json=data)

print("Status code:", response.status_code)
print("Response:", response.json())