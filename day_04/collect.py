# name = input("please tell me your name: ")
# print(name)
name = ''
while name != 'your name':
    name = input("please tell me your name: ")
    if name == "martin":
        continue
    print("keep going!")
    print("nearly got it!")
    if name == 'quit':
        break
        print("never goes here")

print("out of it.")


# flag = True
#
# while flag:
#     answ = input("what do you want? ")
#
#     if answ == 'quit':
#         flag = False