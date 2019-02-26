students = {
    'frederik': 'germany',
    'melissa': 'new zealand',
    'casey': 'united states',
}
# print(students.keys())
# print(students.values())
# print(students.items())

for (name, country) in students.items():
    print(f"{name} is from {country}.")

t = (1, 2)
a, b = t
print(a)
print(b)
