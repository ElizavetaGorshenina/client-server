from subprocess import Popen, CREATE_NEW_CONSOLE


READING_APP_RUN_COMMAND = "python .\client_9_read.py"
WRITING_APP_RUN_COMMAND = "python .\client_9_write.py"

num_app_for_reading = int(input('Введите количество клиентских приложений на чтение чата: '))
num_app_for_writing = int(input('Введите количество клиентских приложений на запись в чат: '))
for _ in range(num_app_for_reading):
    Popen(READING_APP_RUN_COMMAND, creationflags=CREATE_NEW_CONSOLE)
for _ in range(num_app_for_writing):    
    client_write = Popen(WRITING_APP_RUN_COMMAND, creationflags=CREATE_NEW_CONSOLE)
