import requests

endpoint = 'http://localhost:8000/api/products/2/update/'

data = {
    'title': "Hello tbilisi",
    'content': 'tbilissi is a verry verry nice city',
    'price': 4.00
}


get_response = requests.put(endpoint,json=data)

print(get_response.json())