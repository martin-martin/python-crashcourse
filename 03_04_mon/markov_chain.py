import markovify


with open('war_and_peace.txt', 'r') as fin:
    corpus = fin.read()

model = markovify.Text(corpus)

print(model.make_short_sentence(140))

for i in range(5):
    print(model.make_sentence())