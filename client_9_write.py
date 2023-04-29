from socket import *


ADDRESS = ('localhost', 10000)


def set_write(sock, msg):
    sock.send(msg.encode('utf-8'))


def client_write_mainloop():
    print('Приложение на запись в чат')
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(ADDRESS)
        while True:
            msg = input('Ваше сообщение: ')
            if msg == 'exit':
                break
            else:
                set_write(sock, msg)    


if __name__ == '__main__':
    client_write_mainloop()
