import requests

url = "https://stridesafe.onrender.com/predict"

data = {
    "features": [22, 1, 2, 5, 0, 2, 4, 1, 2, 24, 30]  # sample with all encoded values
}

try:
    response = requests.post(url, json=data, timeout=5)
    print("✅ Response:", response.json())
except requests.exceptions.RequestException as e:
    print("❌ Error occurred:", e)

