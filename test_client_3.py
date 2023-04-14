import unittest
from client_3 import get_args, connect_socket
from server_3 import send_data, get_data
import sys
from socket import *

class TestServer(unittest.TestCase):
    def test_get_args_correct(self):
        sys.argv = ['client_3.py', 'localhost', '[7777]']
        args = get_args()
        self.assertEqual((args.addr, args.port), ('localhost', '[7777]'))

    def test_connect_socket(self):
        socket_server = socket(AF_INET, SOCK_STREAM)
        socket_client = socket(AF_INET, SOCK_STREAM)
        address = '127.0.0.1'
        port = 7777
        socket_server.bind((address, port))
        socket_server.listen(1)
        connect_socket(socket_client, address, port)
        self.assertEqual(socket_client.getpeername(), ('127.0.0.1', 7777))
        socket_server.close()
        socket_client.close()


    def test_send_data(self):
        socket_server = socket(AF_INET, SOCK_STREAM)
        socket_client = socket(AF_INET, SOCK_STREAM)
        address = '127.0.0.1'
        port = 7777
        socket_server.bind((address, port))
        socket_server.listen(1)
        socket_client.connect((address, port))
        client, addr = socket_server.accept()
        msg = b'Hello'
        send_data(socket_client, msg)
        received_msg = client.recv(10000)
        self.assertEqual(msg, received_msg)
        socket_server.close()
        socket_client.close()
        client.close()
    

    def test_get_data(self):
        socket_server = socket(AF_INET, SOCK_STREAM)
        socket_client = socket(AF_INET, SOCK_STREAM)
        address = '127.0.0.1'
        port = 7777
        socket_server.bind((address, port))
        socket_server.listen(1)
        socket_client.connect((address, port))
        client, addr = socket_server.accept()
        msg = b'Hello'
        client.send(msg)
        bytes_num = 1024
        data = get_data(socket_client, bytes_num)
        self.assertEqual(data, msg)
        socket_server.close()
        socket_client.close()
        client.close()


if __name__ == '__main__':
    unittest.main()
