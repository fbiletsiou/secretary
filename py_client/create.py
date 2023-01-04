import requests

endpoint = "http://localhost:8000/api/products/24354664/"

# get_response = requests.get(endpoint, params={'abc': 123}, json={"query": "Hello World"})
get_response = requests.get(endpoint)
print(get_response.text)
