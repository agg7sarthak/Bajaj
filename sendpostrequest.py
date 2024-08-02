import requests
import json

url = 'http://127.0.0.1:5000/endpoint'
payload = {
    "user_id": "12345",
    "college_email": "user@college.edu",
    "college_roll": "67890"
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.json())
