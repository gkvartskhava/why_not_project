import requests

endpoint = 'http://localhost:8000/api/products/'

headers = {
    "Authorization" : "Bearer 3203034034271981d4461014ea0339dadf703778"
}

data = {
    "title" : "python is the best",
    "content": "to be or not to be",
    "price" : 100
}


get_response = requests.post(endpoint, json=data, headers = headers)

print(get_response.json())
