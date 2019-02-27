my_list = [1, 2, 3, 5, 42]

new_list = my_list.copy()


#new_list[0] = 2000
print(new_list)
print(my_list)

print(new_list == my_list)
print(new_list is my_list)

tup = (2, 3)
new_tup = tup

print(tup == new_tup)
print(tup is new_tup)