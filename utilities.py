import settings
import json
import os


location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)


def clear():
    """
    Очищает консоль
    Не работает в консоли PyCharm'a
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def get_full_name(people):
    return "%s %s %s" % (people["name"], people["middle_name"], people["surname"])


def search(peoples_list, **kwargs):
    """
    :param peoples_list: список людей, в котором производится поиск. format: [{}, {}, ...]
    :param kwargs: набор именованных параметров поиска
    :return: Возвращает список людей(словари) с заданными именованными параметрами
    """
    return [people for people in peoples_list
            if (people['name'] == kwargs['name'] if kwargs.get('name') else True)
            and (people['surname'] == kwargs['surname'] if kwargs.get('surname') else True)
            and (people['class'] == kwargs['class_room'] or kwargs['class_room'] in people['class']
                 if kwargs.get('class_room') else True)]


def save(data, file_name):
    """
    Сохраняем данные(data) в файл с именем file_name в формате JSON
    :param data: сохраняемые данные
    :type data: any type
    :param file_name: имя файла
    :type file_name: str
    """
    file = open(os.path.join(settings.DATA_DIR, file_name), 'w', encoding="UTF-8")
    file.write(json.dumps(data, ensure_ascii=False))
    file.close()

if __name__ == "__main__":
    pass