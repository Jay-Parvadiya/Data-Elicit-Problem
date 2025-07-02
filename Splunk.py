import requests
import json

splunk_url = 'https://localhost:8088/services/collector'
splunk_token = '10df5d8a-6bf9-4603-a9e5-062ef51d27df'

with open('prices.json', 'r') as f:
    data = json.load(f)

for record in data:
    payload = {
        "event": record,
    }
    headers = {
        "Authorization": f"Splunk {splunk_token}"
    }
    response = requests.post(splunk_url, headers=headers, json=payload, verify=False)
    print(response.text)
