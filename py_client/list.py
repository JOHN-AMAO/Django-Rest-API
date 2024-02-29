import requests
from getpass import getpass

password = getpass()

auth_endpoint = "http://localhost:8000/api/auth/" 

auth_response = requests.post(auth_endpoint, json={"username": "John", "password":password })

print(auth_response.json())

endpoint = "http://localhost:8000/api/products/" 

get_response = requests.get(endpoint)

print(get_response.json())