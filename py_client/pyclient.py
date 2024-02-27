import requests


endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint, json={"name": "John"})

print(get_response.text)