import json
import os


def get_teacher(teacher_str, teachers_data):
    name, surname = teacher_str.split(" ")
    for teacher in teachers_data:
        if teacher["name"] == name and teacher["surname"] == surname:
            return teacher


def get_student(student_str, students_data):
    name, surname = student_str.split(" ")
    for student in students_data:
        if student["name"] == name and student["surname"] == surname:
            return student


def get_full_name(people):
    return "%s %s %s" % (people["name"], people["middle_name"], people["surname"])


DIR = 'data'

students_data = json.load(open(os.path.join(DIR, 'Students.json'), 'r'))
teachers_data = json.load(open(os.path.join(DIR, 'Teachers.json'), 'r'))

class_room = "7 Г"
student_in_class = ['%s %s in %s' % (student["name"], student["surname"], class_room) for student in students_data
                    if student["class"] == class_room]
print(student_in_class)

schools = list(set(map(lambda student: student["school"], students_data)))
print(schools)

surnames = [student["surname"] for student in students_data]
same_surnames = [surname for surname in surnames if surnames.count(surname) > 1]
namesakes = ["%s %s" % (student["name"], student["surname"]) for student in students_data
             if (student["surname"] in same_surnames)]

print(namesakes)

# 2.1
_teacher = "Владимир Вышкин"  # format: 'name surname'
teacher = get_teacher(_teacher, teachers_data)

if teacher:
    teachers_students = [get_full_name(student) for student in students_data
                         if student["school"] == teacher["school"] and student["class"] in teacher["class"]]
    print(teachers_students)
else:
    print('Такой учитель не существует')

# 2.2
_student = "Александр Красный"
student = get_student(_student, students_data)

if student:
    students_teachers = [get_full_name(teacher) for teacher in teachers_data
                         if student["school"] == teacher["school"] and student["class"] in teacher["class"]]
    print(students_teachers)
else:
    print('Такой ученик не существует')

