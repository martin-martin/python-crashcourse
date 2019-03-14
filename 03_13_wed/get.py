import requests

url = "https://en.wikipedia.org/wiki/Ubud"

res = requests.get(url)

#print(res.content)

with open('ubud.html', 'w', encoding='utf-8') as fout:
    fout.write(res.text)