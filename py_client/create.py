import requests

endpoint = 'http://localhost:8000/api/products/'


data = {
    "title" : "georgia is amazing",
    "content":"wakandaa",
    "price" : 10.22,
}


get_response = requests.post(endpoint, json=data)

print(get_response.json())