import requests

endpoint = 'http://localhost:8000/api/products/'


data = {
    "title" : "deep thaughts",
    "content": "to be or not to be",
    "price" : 500000
}


get_response = requests.post(endpoint, json=data)

print(get_response.json())