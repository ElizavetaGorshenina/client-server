from socket import *
from threading import Thread
import time


ADDRESS = ('localhost', 10000)


def set_read(sock):
    while True:
        data = sock.recv(1024)
        print('Ответ:', data.decode('utf-8'))


def set_write(sock):
    while True:
        msg = input('Ваше сообщение: ')
        if msg == 'exit':
            break
        else:
            sock.send(msg.encode('utf-8'))


def client_mainloop():
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(ADDRESS)
        msg_receipt = Thread(target=set_read, args=(sock,))
        msg_receipt.daemon = True
        msg_receipt.start()

        msg_sending = Thread(target=set_write, args=(sock,))
        msg_sending.daemon = True
        msg_sending.start()

        while True:
            time.sleep(1)
            if msg_receipt.is_alive() and msg_sending.is_alive():
                continue
            break


if __name__ == '__main__':
    client_mainloop()
