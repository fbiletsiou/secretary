import requests

endpoint = "http://localhost:8000/api/"

# get_response = requests.get(endpoint, params={'abc': 123}, json={"query": "Hello World"})
get_response = requests.post(endpoint, json={"title": "Hello World"})
print(get_response.text)
