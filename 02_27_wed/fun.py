
# defining a function with the parameter 'name'
def greet(name, nickname):
    print(f"hei {name}, welcome here {nickname}!")


# passing an argument to my function call
greet()


names = ["ben", "michael", "robert", "daniel", "ming"]

for n in names:
    greet(n)
