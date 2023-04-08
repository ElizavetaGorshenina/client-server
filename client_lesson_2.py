'''
Задание 1

Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку
определенных данных из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый
«отчетный» файл в формате CSV. Для этого:
a. Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с
данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения
каждого параметра поместить в соответствующий список. Должно получиться четыре
списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же
функции создать главный список для хранения данных отчета — например, main_data
— и поместить в него названия столбцов отчета в виде списка: «Изготовитель
системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data (также для
каждого файла);
b. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой
функции реализовать получение данных через вызов функции get_data(), а также
сохранение подготовленных данных в соответствующий CSV-файл;
c. Проверить работу программы через вызов функции write_to_csv().
'''


import csv
import re


TASK_1_SOURCE_FILES = ['info_1.txt', 'info_2.txt', 'info_3.txt']
TASK_1_CSV_FILE = 'task_1_file.csv'


def get_data(files: list):
    headers = []
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    main_data = [headers]
    working_dict = {
        'Изготовитель системы': {
            'регулярное выражение для поиска': r'Изготовитель ОС:\s*.+',
            'регулярное выражение для замены': r'Изготовитель ОС:\s*',
            'список': os_prod_list
                                },
        'Название ОС': {
            'регулярное выражение для поиска': r'Название ОС:\s*.+',
            'регулярное выражение для замены': r'Название ОС:\s*',
            'список': os_name_list
                                },
        'Код продукта': {
            'регулярное выражение для поиска': r'Код продукта:\s*.+',
            'регулярное выражение для замены': r'Код продукта:\s*',
            'список': os_code_list
                                },
        'Тип системы': {
            'регулярное выражение для поиска': r'Тип системы:\s*.+',
            'регулярное выражение для замены': r'Тип системы:\s*',
            'список': os_type_list
                                },                                                     
    }

    for k in working_dict.keys():
        headers.append(k)

    for file in files:
        current_file_info = [] 
        with open(file) as f_n:
            for row in f_n:
                for v in working_dict.values():
                    result = re.search(v['регулярное выражение для поиска'], row)
                    if result:
                        result = re.sub(v['регулярное выражение для замены'], '', result.group(0))
                        v['список'].append(result)
                        current_file_info.append(result)
        main_data.append(current_file_info)
    return main_data


def write_to_csv(file: str):
    with open(file, 'w', encoding='utf-8') as f_n:
        f_n_writer = csv.writer(f_n)
        for row in get_data(TASK_1_SOURCE_FILES):
            f_n_writer.writerow(row)


write_to_csv(TASK_1_CSV_FILE)


'''
Задание 2

 Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с
информацией о заказах. Написать скрипт, автоматизирующий его заполнение данными. Для
этого:
a. Создать функцию write_order_to_json(), в которую передается 5 параметров — товар
(item), количество (quantity), цена (price), покупатель (buyer), дата (date). Функция
должна предусматривать запись данных в виде словаря в файл orders.json. При
записи данных указать величину отступа в 4 пробельных символа;
b. Проверить работу программы через вызов функции write_order_to_json() с передачей
в нее значений каждого параметра.
'''


import json


def write_order_to_json(item, quantity, price, buyer, date):
    dict_to_json = {
    "item": item,
    "quantity": quantity,
    "price": price,
    "buyer": buyer,
    "date": date
    }

    with open('orders.json') as f_n:
        f_n_content = f_n.read()
        objs = json.loads(f_n_content)

    objs["orders"].append(dict_to_json)

    with open('orders.json', 'w') as f_n:
       json.dump(objs, f_n, indent=4)


write_order_to_json('чайник', 1, 2500, 'Liza', '04.04.2023')
write_order_to_json('чай', 2, 250, 'Liza', '05.04.2023')


'''
Задание 3

Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий
сохранение данных в файле YAML-формата. Для этого:
a. Подготовить данные для записи в виде словаря, в котором первому ключу
соответствует список, второму — целое число, третьему — вложенный словарь, где
значение каждого ключа — это целое число с юникод-символом, отсутствующим в
кодировке ASCII (например, €);
b. Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а
также установить возможность работы с юникодом: allow_unicode = True;
c. Реализовать считывание данных из созданного файла и проверить, совпадают ли они
с исходными.

'''


import yaml


movie = {
    "actors": ["Tom Holland", "Jessica Cruse", "Kelly Smith"],
    "year": 2023,
    "main info": {
        "name": "Furious Chipmunk",
        "director": "Paul Oldridge"
    },
    "box office": "63000€"
}

with open('file.yaml', 'w') as f_n:
    yaml.dump(movie, f_n, allow_unicode=True, default_flow_style=False)

with open('file.yaml') as f_n:
    movie_yaml_data = yaml.load(f_n, Loader=yaml.Loader)

data_equality_flag = 1
for k in movie.keys():
    if movie[k] != movie_yaml_data[k]:
        data_equality_flag = 0
if data_equality_flag == 1:
    print("Данные совпадают с исходными")
else:
    print("Данные НЕ совпадают с исходными")
