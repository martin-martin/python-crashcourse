import requests


login_url = "https://my.freecycle.org/login"
scrape_url = "https://my.freecycle.org/home/groups"

payload = {
    'username': 'martin-martin',
    'pass': 'bali2019',
}

with requests.Session() as session:
#session = requests.Session()
    post = session.post(login_url, data=payload)
    print(post.status_code)
    res = session.get(scrape_url)
    print(res.status_code)
#session.close()

with open('free.html', 'w') as fout:
    fout.write(res.text)
