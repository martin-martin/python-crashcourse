recipe = {'carrots': 4, 'apples': 10, 'water': 10}
#print(recipe['apples'])

students = [{'name': 'frederik',
                'age': 21,
                'nationality': ['German', 'Indonesian'],
                'student_ID': 1},
            {'name': 'melissa',
                'age': 218,
                'nationality': 'NewZealandish',
                'student_ID': 2},
            {'name': 'casey',
             'age': 10,
             'nationality': 'United States',
             'student_ID': 3},
            ]

for student in students:
    print(student['age'])


#print(students[0]['nationality'][0])

students[1]['home country'] = None
print(students[1])

home = students[1].pop('home country')

print(students[1])
print(home)


#print(recipe)
