import requests

url = 'http://127.0.0.1:5000/endpoint'

response = requests.get(url)

print(response.json())
