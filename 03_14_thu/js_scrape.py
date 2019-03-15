from requests_html import HTMLSession


url = "https://www.instagram.com/martin.breuss/"
session = HTMLSession()
r = session.get(url)
r.html.render()  # parses JavaScript!

print(r.html.text)
for link in r.html.absolute_links:
    print(link)
