import json
from utilities import search, get_full_name, location, clear, save

school_data = []
students_data = []
teachers_data = []


def load_data():
    global school_data
    global students_data
    global teachers_data

    with open(location('data/school.json')) as f:
        school_data = json.load(f)

    with open(location('data/Students.json')) as f:
        students_data = json.load(f)

    with open(location('data/Teachers.json')) as f:
        teachers_data = json.load(f)


def menu_do(menu, clean=True, **kwargs):
    while True:
        if clean:
            clear()
            print("*" * 24)
            print("* Welcome to %s %s *" % (school_data['number'], school_data['type']))
            print("*" * 24)
            print("MENU > ", kwargs.get("sub_menu", ''))
        for number, el in enumerate(menu, start=1):
            print("%s. %s" % (number, el["text"]))
        choice = int(input(": "))
        menu_select = menu[choice - 1]
        if menu_select.get("do"):
            if menu_select["do"](*menu_select['args'] if menu_select.get('args') else ('',)):
                break
        else:
            menu_do(menu_select["sub_menu"], sub_menu=menu_select['text'])


def about_students(*args):
    for class_room in school_data["classes"]:
        print("Ученики '%s' класса: " % class_room)
        for num, student in enumerate(search(students_data, class_room=class_room), start=1):
            print("    %s) %s" % (
                num, get_full_name(student)))  # TODO(complete): Добавить нумерацию учеников для каждого класса
        print("-" * 24)
    input("Нажмите Enter для возврата в предыдущее меню")


def about_techers(*args):
    for class_room in school_data["classes"]:
        print("Учителя '%s' класса: " % class_room)
        for num, teacher in enumerate(search(teachers_data, class_room=class_room), start=1):
            print("    %s) %s" % (num, get_full_name(teacher)))
        print("-" * 24)
    input("Нажмите Enter для возврата в предыдущее меню")


def about_classes(*args):
    clear()
    # head
    print("Все классы нашей школы")
    print("||", " || ".join(school_data['classes']), "||")
    print()
    class_room = input("Введите класс, для подробной информации по нему \n"
                       " (или Enter для возврата в предыдущее меню):")
    if class_room in school_data["classes"]:
        print("\nИнформация по %s классу:" % class_room)
        # TODO(complete): вывести всех учеников и учителей указанного класса
        print("     Ученики:")
        for student in search(students_data, class_room=class_room):
            print("         ", get_full_name(student))
        print("     Учителя:")
        for teacher in search(teachers_data, class_room=class_room):
            print("         ", get_full_name(teacher))
        input("Нажмите Enter для возврата в предыдущее меню")
        return
        # TODO(complete): Сделать возврат в предыдущее меню(во всех местах программы).
        # TODO(complete):Выход из программы только по пункту "выйти"
    # FIXME(complete): сообщить, если выбран несуществующий класс
    elif not class_room:
        return
    print("Указан несуществующий класс")
    input("Нажмите Enter для продолжения")


def edit_student(*args):
    clear()
    print("     MENU > Редактировать > Ученика")
    for num, student in enumerate(students_data, start=1):
        print("%s) %s || %s" % (num, get_full_name(student), student['class']))
    student_num = int(input('Укажите номер ученика(или 0(НОЛЬ), для создания нового): '))
    if student_num == 0:
        create_student()
        return
    try:
        student = students_data[student_num - 1]
    except IndexError:
        print('Несуществующий пункт меню')
        input("Нажмите Enter для продолжения")
        return
    print()
    print("Вы выбрали %s " % get_full_name(student))
    for key, value in student.items():
        if key in ['name', 'surname', 'middle_name', 'id']:
            continue
        print("     %s: %s" % (key, value))
    print()
    sum_menu = [
        {
            'text': 'Удалить ученика',
            'do': del_student,
            'args': (student,)
        },
        {
            'text': 'Перевести в другой класс',
            'do': change_student_class,
            'args': (student,)
        },
        {
            'text': 'назад',
            'do': lambda x: True
        }
    ]
    menu_do(sum_menu, clean=False)


def create_student(*args):
    new_student = {}
    next_id = students_data[-1]['id'] + 1
    print("Укажите параметры нового ученика: ")
    new_student['name'] = input('Имя: ')
    new_student['surname'] = input('Фамилию: ')
    new_student['middle_name'] = input('Отчество: ')
    new_student['class'] = ''
    new_student['school'] = school_data['number'] + ' ' + school_data['type']
    new_student['id'] = next_id
    students_data.append(new_student)
    save(students_data, 'Students.json')
    print('Ученик успешно создан и сохранен')
    input("Нажмите Enter для продолжения")


def del_student(*args):
    students_data.remove(args[0])
    save(students_data, 'Students.json')


def change_student_class(*args):
    print("||", " || ".join(school_data['classes']), "||")
    new_class = input("Укажите новый класс: ")
    if new_class not in school_data['classes']:
        print('нельзя перевести ученика в несуществующий класс')
        input("Нажмите Enter для возврата в предыдущее меню")
        return True
    student = args[0]
    student['class'] = new_class
    save(students_data, 'Students.json')


def edit_teacher(*args):
    clear()
    print("*" * 24)
    print("* Welcome to %s %s *" % (school_data['number'], school_data['type']))
    print("*" * 24)
    print("     MENU > Редактировать > Учителя")
    # Заглушка
    print("Данный пункт находится в разработке")
    input("Нажмите Enter для возврата в предыдущее меню")


# def info_students():
# for class_room in school_data["classes"]:
# print("Ученики '%s' класса: " % class_room)
# for student in search(students_data, class_room=class_room):
#             # FIXME: учесть(во всей программе), в файле могут быть ученики из других школ
#             print("     ", get_full_name(student))  # TODO: Добавить нумерацию учеников для каждого класса
#         print("-" * 24)
#     input("Нажмите Enter для возврата в предыдущее меню")


def edit_delete_class(*args):
    print("Все классы нашей школы")
    print("||", " || ".join(school_data['classes']), "||")
    class_room = input("Введите класс: ")
    if class_room in school_data["classes"]:
        # 1
        school_data['classes'].remove(class_room)
        save(school_data, 'school.json')
        # 2
        for teacher in teachers_data:
            if class_room in teacher['class']:
                teacher['class'].remove(class_room)
        save(teachers_data, 'Teachers.json')
        # 3
        for student in students_data:
            if class_room == student['class']:
                student['class'] = ''
        save(students_data, 'Students.json')

        # TODO: 1. Удалить класс из school.json
        # TODO: 2. Удалить класс у всех учителей
        # TODO: 3. Заменить класс у всех учеников на '' (считается что ученик ожидает перевод в новый класс)
        # TODO: 4. Не забыть обновить информацию в файлах
        # TODO: 5. Сделать изменения в меню 'MENU > Информация > Об учениках' (вывести учеников без классов)

    else:
        print('Вы ввели несуществующий класс')
        # TODO: и предложить ввести класс повторн


def edit_create_class(*args):
    new_class = input("Введите название нового класса: ")
    school_data['classes'].append(new_class)
    save(school_data, 'school.json')


def end(*args):
    print("Goodbye")
    return True


load_data()

menu = [
    {
        "text": "Информация",
        # "do": info,
        "sub_menu": [
            {
                "text": "О классах",
                "do": about_classes
            },
            {
                "text": "Об учениках",
                "do": about_students
            },
            {
                "text": "Об учителях",
                "do": about_techers
            },
            {
                "text": "назад",
                "do": lambda x: True
            }
        ]
    },
    {
        "text": "Редактировать",
        "sub_menu": [
            {
                "text": "Класс",
                "sub_menu": [
                    {
                        "text": "Удалить существующий",
                        "do": edit_delete_class
                    },
                    {
                        "text": "Создать новый",
                        "do": edit_create_class
                    },
                    {
                        "text": "назад",
                        "do": lambda x: True
                    },
                ]
            },
            {
                "text": "Ученика",
                "do": edit_student
            },
            {
                "text": "Учителя",
                "do": edit_teacher
            },
            {
                "text": "назад",
                "do": lambda x: True
            }
        ]
    },
    {
        "text": "Выход",
        "do": end
    }
]

menu_do(menu)
