import select
from socket import *


def read_requests(r_clients, all_clients):
    requests = {}
    for sock in r_clients:
        try:
            data = sock.recv(1024).decode('utf-8')
            if data:
                requests[sock] = data
                print('Received request: ', data)
        except:
            print('Клиент {} {} отключился'.format(sock.fileno(), sock.getpeername()))
            all_clients.remove(sock)
    return requests


def write_responses(requests, w_clients, all_clients):
    for sock in w_clients:
        for a_sock, a_mes in requests.items():
            if a_sock != sock:
                try:
                    resp = (a_mes + '\n').encode('utf-8')
                    sock.send(resp)
                except:
                    print('Клиент {} {} отключился'.format(sock.fileno(),
                    sock.getpeername()))
                    sock.close()
                    all_clients.remove(sock)


def server_mainloop():
    address = ('', 10000)
    clients = []
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(address)
    s.listen(5)
    s.settimeout(0.5)
    while True:
        try:
            conn, addr = s.accept()
        except OSError as e:
            pass
        else:
            print("Получен запрос на соединение от %s" % str(addr))
            clients.append(conn)
            print(clients)
        finally:
            wait = 5
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass
            requests = read_requests(r, clients)
            if requests:
                write_responses(requests, w, clients)


print('Cервер запущен!')
server_mainloop()
