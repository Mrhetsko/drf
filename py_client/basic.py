import requests

# endpoint = 'https://httpbin.org/status/200/'
# endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:8000/api/'
responce = requests.post(endpoint, json={'title': 'Hello My World'})
# print(responce.text)
print(responce.json())
# print(responce.status_code)