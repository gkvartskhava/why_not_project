import requests


endpoint = "https://httpbin.org/status/200"
endpoint = 'https://httpbin.org/anything'
endpoint = 'https://httpbin.org/status/200'



get_response = requests.get(endpoint)

print(get_response.text)

# print(get_response.json())
# HTTP request  => HTML
# REST API HTTP REQUEST  => JSON