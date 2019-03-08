# list comprehensions
my_list = [1, 2, 3, 5, 42]

new_list = [i+1 for i in my_list if not i % 2 == 0]
print(new_list)


new_list = []
for i in my_list:
    if i % 2 != 0:
        new_list.append(i+1)

print(new_list)

























# my_list = [1, 2, 3, 5, 42]
#
# new_list = []
# for x in my_list:
#     y = x**2
#     new_list.append(y)
#
# print(new_list)
#
#
# squared = [x**2 for x in my_list]
# print(squared)
#
#
# square_even = [x**2 for x in my_list if x % 2 == 0]
# print(square_even)