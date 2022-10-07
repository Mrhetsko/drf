import requests

endpoint = "http://localhost:8000/api/products/1/update/" 

data = {
    "title": "Hello my  world",
    "price": 12.98
}

get_response = requests.put(endpoint, json=data) 
print(get_response.json())