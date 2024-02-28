import requests


endpoint = "http://localhost:8000/api/products/1/update" 

data = {'title': ' def not Hello world', 'content': 'this is a test', 'price': '0.00', 'sale_price': '0.00', 'get_discount': 122}

get_response = requests.put(endpoint, json=data)

print(get_response.json())