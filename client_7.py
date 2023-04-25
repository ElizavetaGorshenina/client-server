from socket import *


ADDRESS = ('localhost', 10000)


def set_read(sock):
    data = sock.recv(1024)
    return data.decode('utf-8')


def set_write(sock, msg):
    sock.send(msg.encode('utf-8'))


def client_mainloop():
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(ADDRESS)
        while True:
            sock_option = input('Принять/отправить сообщение: ')
            if sock_option == 'exit':
                break
            if sock_option == 'r':
                data = set_read(sock)
                print('Ответ:', data)
            if sock_option == 'w':
                msg = input('Ваше сообщение: ')
                set_write(sock, msg)    


if __name__ == '__main__':
    client_mainloop()
