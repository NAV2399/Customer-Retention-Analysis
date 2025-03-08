import requests

url = "http://127.0.0.1:8000/predict_churn"
data = {
    "recency": 30,
    "frequency": 5,
    "monetary": 1000.0
}

response = requests.post(url, json=data)
print(response.json())