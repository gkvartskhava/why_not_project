import requests


#endpoint = "https://httpbin.org/status/200"
# endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/api/'




get_response = requests.post(endpoint, params={'test':123}, json={'query':'Hello world'})


print(get_response.text)
# print(get_response.headers)
#print(get_response.status_code)

# print(get_response.json())
# HTTP request  => HTML
# REST API HTTP REQUEST  => JSON

