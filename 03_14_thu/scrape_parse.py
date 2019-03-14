from requests_html import HTMLSession


url = "https://en.wikipedia.org/wiki/Ubud"
session = HTMLSession()
r = session.get(url)

for link in r.html.absolute_links:
    print(link)

# using CSS selectors
history = r.html.find('#Buildings', first=True)  # first=True because otherwise it returns a list

# or using XPATH
content = r.html.xpath('//*[@id="mw-content-text"]/div', first=True)

ps = content.find('p')

for p in ps:
    print(p.text, end='\n\n')
