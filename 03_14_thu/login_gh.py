import requests


login_url = "https://github.com/session"
scrape_url = "https://github.com/martin-martin"

payload = {
    'login': 'your-username',
    'password': 'your-password',
    'authenticity_token': 'fetch-that-token'
}

with requests.Session() as session:
#session = requests.Session()
    post = session.post(login_url, data=payload)
    print(post.status_code)
    res = session.get(scrape_url)
    print(res.status_code)
#session.close()w

with open('gh.html', 'w') as fout:
    fout.write(res.text)
