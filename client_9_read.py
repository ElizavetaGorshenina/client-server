from socket import *


ADDRESS = ('localhost', 10000)


def set_read(sock):
    data = sock.recv(1024)
    return data.decode('utf-8')


def client_read_mainloop():
    print('Приложение на чтение чата')
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(ADDRESS)
        while True:
            data = set_read(sock)
            print('Ответ:', data)


if __name__ == '__main__':
    client_read_mainloop()
