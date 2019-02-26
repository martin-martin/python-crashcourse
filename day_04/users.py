pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

print(pets)

catlist = []
while 'cat' in pets:
    pets.remove('cat')
    catlist.append('cat')

print(pets)
print(catlist)
