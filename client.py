'''
Задание 1

Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
проверить тип и содержание соответствующих переменных. Затем с помощью
онлайн-конвертера преобразовать строковые представление в формат Unicode и также
проверить тип и содержимое переменных.
'''

print('ЗАДАНИЕ 1')
task_1_words = ['разработка', 'сокет', 'декоратор']
for word in task_1_words:
    print(word)
    print(type(word))
    word_in_bytes = word.encode('utf-8')
    print(word_in_bytes)
    print(type(word_in_bytes))


'''
Задание 2

Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в
последовательность кодов (не используя методы encode и decode) и определить тип,
содержимое и длину соответствующих переменных
'''

print('ЗАДАНИЕ 2')
task_2_words = ['class', 'function', 'method']
for word in task_2_words:
    word_in_bytes = bytes(word, 'utf-8')
    print(type(word_in_bytes))
    print(word_in_bytes)
    print(len(word_in_bytes))


'''
Задание 3

Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в
байтовом типе.

-----
ОТВЕТ: слова «класс» и «функция» невозможно записать в байтовом типе, т.к. они состоят из 
символов, не относящийся к ASCII.
'''

print('ЗАДАНИЕ 3')
task_3_words = ['attribute', 'класс', 'функция', 'type']
for word in task_3_words:
    try:
        word_in_bytes = word.encode('ascii')
    except UnicodeEncodeError:
        print(f"The word '{word}' can't be written in byte type as bytes can only contain ASCII literal characters.")


'''
Задание 4

Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
строкового представления в байтовое и выполнить обратное преобразование (используя
методы encode и decode).
'''

print('ЗАДАНИЕ 4')
task_4_words = ['разработка', 'администрирование', 'protocol', 'standard']
for word in task_4_words:
    word_in_bytes = word.encode('utf-8')
    print(word_in_bytes)
    word = word_in_bytes.decode('utf-8')
    print(word)


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


task_6_strings = ['сетевое программирование', 'сокет', 'декоратор']
def_coding = locale.getpreferredencoding()
print(def_coding)

f_n = open("test_file.txt", "w+")
for string in task_6_strings:
    f_n.write(f'{string}\n')
f_n.close()
with open('test_file.txt', encoding='utf-8') as f_n:
    try:
        for el_str in f_n:
            print(el_str)
    except UnicodeDecodeError:
        print('UnicodeDecodeError')
