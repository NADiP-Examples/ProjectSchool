# *********
# Задание
# *********
# Допишите код програмы в соответствии с примечаниями (TODO и FIXME) в коде программы
# Реализовать нужно только те пункты меню, о которых сказано в примечаниях
# Все неработающие пункты(если такие останутся) пометьте каким-нить символом(например *) и сделайте к ним заглушки
# TОDО-шки не удаляйте, а меняйте TODO --> TODO(complete)
# Меняйте структуру программы, если это нужно
# Дописывайте вспомогателные функции
# Постарайтесь убрать существующие дублирования кода(где это возможно) и избежать дальнейших повторений
# TODO* - наиболее сложные задачи

# *********
# Доп. Задания (для желающих и тех, у кого осталось время)
# *********
# 1. Напишите скрипт(программу), которая будет удалять всех учеников и учителей из файлов с данными, не имеющих отношения
# к текущей школе и текущим класса (указанным в school.json)
# 2. Сделайте функцию обертку, для удобного вывода цветного текста
# 3. Разукрасьте текст программы, сделав его удобнее для восприятия

import os
import json
from utilities import location, clear, get_full_name, search


def load_data():
    global school_data
    global students_data

    with open(location('data/school.json')) as f:
        school_data = json.load(f)

    with open(location('data/Students.json')) as f:
        students_data = json.load(f)

# Load data
load_data()

# MAIN

clear()
# Про цветной текст ищите в гугле
print("\033[1;34m*\033[1;m" * 24)
print("\033[1;34m* Welcome to %s %s *\033[1;m" % (school_data['number'], school_data['type']))
print("\033[1;34m*\033[1;m" * 24)
print("     MENU")
print("1. Информация")
print("2. Редактировать")
print("3. Выйти")
choice = input(':')

if choice == '1':  # INFO
    clear()
    print("*" * 24)
    print("* Welcome to %s %s *" % (school_data['number'], school_data['type']))
    print("*" * 24)
    print("     MENU > Информация")
    print("1. О классах")
    print("2. Об учениках")
    print("3. Об учителях")
    print("4. Назад")
    choice = input(':')
    if choice == '1':
        clear()
        print("*" * 24)
        print("* Welcome to %s %s *" % (school_data['number'], school_data['type']))
        print("*" * 24)
        print("     MENU > Информация > О классах")
        print("Все классы нашей школы")
        print("||", " || ".join(school_data['classes']), "||")
        print()
        class_room = input("Введите класс, для подробной информации по нему \n"
                           " (или Enter для возврата в предыдущее меню):")
        if class_room in school_data["classes"]:  # FIXME: сообщить, если выбран несуществующий класс
            print("\nИнформация по %s классу:" % class_room)
            # TODO: вывести всех учеников и учителей указанного класса
            print("     Учителя: ...")
            print("     Ученики: ...")
            input("Нажмите Enter для возврата в предыдущее меню")
            # TODO*: Сделать возврат в предыдущее меню(во всех местах программы).
            # TODO:Выход из программы только по пункту "выйти"

    elif choice == '2':
        clear()
        print("*" * 24)
        print("* Welcome to %s %s *" % (school_data['number'], school_data['type']))
        print("*" * 24)
        print("     MENU > Информация > Об учениках")
        for class_room in school_data["classes"]:
            print("Ученики '%s' класса: " % class_room)
            for student in search(students_data, class_room=class_room):
                # FIXME: учесть(во всей программе), в файле могут быть ученики из других школ
                print("     ", get_full_name(student))  # TODO: Добавить нумерацию учеников для каждого класса
            print("-" * 24)
        input("Нажмите Enter для возврата в предыдущее меню")
    elif choice == '3':
        clear()
        print("*" * 24)
        print("* Welcome to %s %s *" % (school_data['number'], school_data['type']))
        print("*" * 24)
        print("     MENU > Информация > Об учителях")
        print(' ... ')
        # TODO: дописать вывод по аналогии с учениками
        input("Нажмите Enter для возврата в предыдущее меню")


elif choice == '2':
    clear()
    print("*" * 24)
    print("* Welcome to %s %s *" % (school_data['number'], school_data['type']))
    print("*" * 24)
    print("     MENU > Редактировать")
    print("1. Класс")
    print("2. Ученика")
    print("3. Учителя")
    choice = input(": ")
    if choice == '1':
        clear()
        print("*" * 24)
        print("* Welcome to %s %s *" % (school_data['number'], school_data['type']))
        print("*" * 24)
        print("     MENU > Редактировать > Класс")
        print("     Классы: ")
        print("     ||", " || ".join(school_data['classes']), "||")
        print()
        print("1. Удалить существующий")
        print("2. Создать новый")
        print("3. Назад")  # TODO: Реализовать ВСЕ(во всей программе) пункты 'назад'

        choice = input(": ")
        if choice == '1':
            class_room = input("Введите класс: ")
            if class_room in school_data["classes"]:
                pass
                # TODO: 1. Удалить класс из school.json
                # TODO: 2. Удалить класс у всех учителей
                # TODO: 3. Заменить класс у всех учеников на '' (считается что ученик ожидает перевод в новый класс)
                # TODO: 4. Не забыть обновить информацию в файлах
                # TODO: 5. Сделать изменения в меню 'MENU > Информация > Об учениках' (вывести учеников без классов)

        else:
            print('Вы ввели несуществующий класс')
            # TODO: и предложить ввести класс повторно
    elif choice == '2':
        clear()
        print("*" * 24)
        print("* Welcome to %s %s *" % (school_data['number'], school_data['type']))
        print("*" * 24)
        print("     MENU > Редактировать > Ученика")
        for num, student in enumerate(students_data):
            print("%s) %s || %s" % (num, get_full_name(student), student['class']))
        student_num = input('Укажите номер ученика(или НОЛЬ, для создания нового): ')
        print()
        print("Вы выбрали %s " % 'unknown')  # TODO: Указать выбранного ученика и отобразить по нему полную информацию
        # FIXME: не забыть обработать ввод номера несуществующего ученика
        print('1. Удалить ученика')
        print('2. Перевести в другой класс')
        print('3. Назад')
        # TODO: реализовать удаление и перевод ученика
        # TODO*: реализовать создание нового ученика с вводом всех необходимых параметров
        # TODO: не забыть, нельзя задать ученику несуществующий класс
    elif choice == '3':
        clear()
        print("*" * 24)
        print("* Welcome to %s %s *" % (school_data['number'], school_data['type']))
        print("*" * 24)
        print("     MENU > Редактировать > Учителя")
        # Заглушка
        print("Данный пункт находится в разработке")
        input("Нажмите Enter для возврата в предыдущее меню")



elif choice == '3':
    print("Goodbye")
else:
    print("Error: Not correct menu item")


