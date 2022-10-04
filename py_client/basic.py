import requests

# endpoint = 'https://httpbin.org/status/200/'
endpoint = 'https://httpbin.org/anything'

responce = requests.get(endpoint, json={"query": "Hello world"})
# print(responce.text)
# print(responce.json())
print(responce.status_code)
