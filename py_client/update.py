import requests

endpoint = 'http://localhost:8000/api/products/13/update/'

data = {
    'title': "Hello tbilisi",
    'content': 'zugdidi is a verry verry nice city',
    'price': 404.00
}


get_response = requests.put(endpoint,json=data)

print(get_response.json())