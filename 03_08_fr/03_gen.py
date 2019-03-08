# generator expressions

my_list = [1, 2, 3, 5, 42]

new_li = [x+1 for x in my_list]
print(new_li)

gen = (x+1 for x in my_list)
print(gen)

for x in gen:
    print(x)






















# my_list = [1, 2, 3, 5, 42]
#
#
# li_ = [x**2 for x in my_list]
#
# gen = (x**2 for x in my_list)
#
# print(li_)
# print(gen)
#
#
# for x in gen:
#     print(x)