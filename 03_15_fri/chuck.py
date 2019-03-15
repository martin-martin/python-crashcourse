import requests


url = "https://api.chucknorris.io/jokes/random?category=dev"
res = requests.get(url)


formatted = res.json()
print(type(formatted))
print(formatted['value'])