import requests

for _ in range(10):
    response = requests.get('http://load_balancer:8080')
    print(response.text)
