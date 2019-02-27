student_1 = {'name': 'frederik',
             'nationality': 'Germany',
             'student_ID': 1}
student_2 = {'name': 'melissa',
             'nationality': 'New Zealand',
             'student_ID': 2}
student_3 = {'name': 'casey',
             'nationality': 'United States',
             'student_ID': 3}

students = [student_1, student_2, student_3]

for student in students:
    print(student['nationality'])
