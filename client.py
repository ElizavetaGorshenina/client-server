'''
Задание 1

Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
проверить тип и содержание соответствующих переменных. Затем с помощью
онлайн-конвертера преобразовать строковые представление в формат Unicode и также
проверить тип и содержимое переменных.
'''

print('ЗАДАНИЕ 1')
task_1_w_1 = 'разработка'
task_1_w_2 = 'сокет'
task_1_w_3 = 'декоратор'
print(task_1_w_1)
print(task_1_w_2)
print(task_1_w_3)
print(type(task_1_w_1))
print(type(task_1_w_2))
print(type(task_1_w_3))
task_1_w_1_b = task_1_w_1.encode('utf-8')
task_1_w_2_b = task_1_w_2.encode('utf-8')
task_1_w_3_b = task_1_w_3.encode('utf-8')
print(task_1_w_1_b)
print(task_1_w_2_b)
print(task_1_w_3_b)
print(type(task_1_w_1_b))
print(type(task_1_w_2_b))
print(type(task_1_w_3_b))


'''
Задание 2

Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
последовательность кодов (не используя методы encode и decode) и определить тип,
содержимое и длину соответствующих переменных
'''

print('ЗАДАНИЕ 2')
task_2_w_1 = 'class'
task_2_w_2 = 'function'
task_2_w_3 = 'method'
task_2_w_1_b = bytes(task_2_w_1, 'utf-8')
task_2_w_2_b = bytes(task_2_w_2, 'utf-8')
task_2_w_3_b = bytes(task_2_w_3, 'utf-8')
print(type(task_2_w_1_b))
print(type(task_2_w_2_b))
print(type(task_2_w_3_b))
print(task_2_w_1_b)
print(task_2_w_2_b)
print(task_2_w_3_b)
print(len(task_2_w_1_b))
print(len(task_2_w_2_b))
print(len(task_2_w_3_b))


'''
Задание 3

Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
байтовом типе.

-----
ОТВЕТ: слова «класс» и «функция» невозможно записать в байтовом типе, т.к. они состоят из 
символов, не относящийся к ASCII.
'''

print('ЗАДАНИЕ 3')
task_3_w_1 = 'attribute'
task_3_w_2 = 'класс'
task_3_w_3 = 'функция'
task_3_w_4 = 'type'
task_3_w_1_b = bytes(task_3_w_1, 'utf-8')
task_3_w_2_b = bytes(task_3_w_2, 'utf-8')
task_3_w_3_b = bytes(task_3_w_3, 'utf-8')
task_3_w_4_b = bytes(task_3_w_4, 'utf-8')
print(task_3_w_1_b)
print(task_3_w_2_b)
print(task_3_w_3_b)
print(task_3_w_4_b)


'''
Задание 4

Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
строкового представления в байтовое и выполнить обратное преобразование (используя
методы encode и decode).
'''

print('ЗАДАНИЕ 4')
task_4_w_1 = 'разработка'
task_4_w_2 = 'администрирование'
task_4_w_3 = 'protocol'
task_4_w_4 = 'standard'
task_4_w_1_b = task_4_w_1.encode('utf-8')
task_4_w_2_b = task_4_w_2.encode('utf-8')
task_4_w_3_b = task_4_w_3.encode('utf-8')
task_4_w_4_b = task_4_w_4.encode('utf-8')
print(task_4_w_1_b)
print(task_4_w_2_b)
print(task_4_w_3_b)
print(task_4_w_4_b)
task_4_w_1 = task_4_w_1_b.decode('utf-8')
task_4_w_2 = task_4_w_2_b.decode('utf-8')
task_4_w_3 = task_4_w_3_b.decode('utf-8')
task_4_w_4 = task_4_w_4_b.decode('utf-8')
print(task_4_w_1)
print(task_4_w_2)
print(task_4_w_3)
print(task_4_w_4)


'''
Задание 5

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
байтовового в строковый тип на кириллице.
'''

print('ЗАДАНИЕ 5')

import subprocess


args_yandex = ['ping', 'yandex.ru']
subproc_ping_yandex = subprocess.Popen(args_yandex, stdout=subprocess.PIPE)
for line in subproc_ping_yandex.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))

args_youtube = ['ping', 'youtube.com']
subproc_ping_youtube = subprocess.Popen(args_youtube, stdout=subprocess.PIPE)
for line in subproc_ping_youtube.stdout:
    line = line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))


'''
Задание 6

Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
'''

print('ЗАДАНИЕ 6')

import locale


def_coding = locale.getpreferredencoding()
print(def_coding)

with open('test_file.txt', encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str)
