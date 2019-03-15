from requests_html import HTMLSession


s = HTMLSession()

login_url = "https://my.freecycle.org/login"
scrape_url = "https://my.freecycle.org/home/groups"

payload = {
    'username': 'martin-martin',
    'pass': 'bali2019',
}

post = s.post(login_url, data=payload)
print(post.status_code)
r = s.get(scrape_url)
print(r.status_code)

for link in r.html.absolute_links:
    if 'Denver' in link and link.endswith('CO') and link.startswith('http://'):
        #print(link)
        posts_url = link

res = s.get(posts_url)
print(res.status_code)
for post in res.html.find('a'):
    print(post.text)

