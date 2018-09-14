from college import Student, Group, Teacher

print('*' *25)
students_23 = Student.import_from_file('23_group.src')
group_23 = Group('23', 'Прикладная информатика 09.02.05')
group_23.add_students(students_23)
[print(el, el.group) for el in students_23]

print('*' *25)
students_33 = Student.import_from_file('33_group.src')
group_33 = Group('33', 'Прикладная информатика 09.02.05')
group_33.add_students(students_33)
[print(el, el.group) for el in students_33]

print('*' *25)
teachers = Teacher.import_from_file('teachers.src')
[print(el) for el in teachers]