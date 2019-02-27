my_list = [1, 2, 1, 42, 3, 5, 42]

my_list.insert(2, 55)

#print(my_list.pop(4))

new_list = list(set(my_list)).remove(42)
print(new_list)

unique_list = list(set(my_list))
#print(my_list.remove(42))
unique_list.remove(42)

print(unique_list)
print(my_list)
