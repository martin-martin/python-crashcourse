import requests

#num = int(input('input number'))
num = 80
params = {
    'type': 'trivia',
    'notfound': 'floor',
}


url = f"http://numbersapi.com/{num}?type=trivia&notfound=floor&fragment"
print("hello")
#url = f"http://numbersapi.com/{num}?{'&'.join([key + '='+ value for key, value in params.items()])}&fragment"



print(url)
r = requests.get(url)

#print(type(r))
# some program
#print(r.text)
print(f"This opponent has more lives than {r.text}")