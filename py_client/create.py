import requests

endpoint = 'http://localhost:8000/api/products/'


data = {
    "title" : "deep thaughts",
    
    "price" : 100000
}


get_response = requests.post(endpoint, json=data)

print(get_response.json())