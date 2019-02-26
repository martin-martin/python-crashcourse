locations = ["indonesia", "spain", "thailand", "mexico", "usa"]

# membership operators

# in
# not in

print('bali' not in locations)

my_list = [1, 2, 3, 5, 42]
even = []
for num in my_list:
    if num % 2 == 0:
        even.append(num)

print(even)

not_even = []
for num in my_list:
    if num not in even:
        not_even.append(num)

print(not_even)
