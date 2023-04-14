import unittest
from server_3 import get_args, init_tcp_socket, decode_and_load_bytes, encode_and_dump_dict, bind_socket, accept_connestion_socket, get_data, send_data
import sys
from socket import *
import json


class TestServer(unittest.TestCase):
    def test_get_args_correct(self):
        sys.argv = ['server_3.py', '-p=7777', '-a=localhost']
        args = get_args()
        self.assertEqual((args.address, args.port), ('localhost', 7777))


    def test_get_args_empty(self):
        sys.argv = ['server_3.py']
        args = get_args()
        self.assertEqual((args.address, args.port), ('', 7777))

    
    def test_init_tcp_socket(self):
        a_socket = init_tcp_socket()
        self.assertEqual((a_socket.family, a_socket.type), (AddressFamily.AF_INET, SocketKind.SOCK_STREAM))
        a_socket.close()


    def test_bind_socket(self):
        a_socket = socket(AF_INET, SOCK_STREAM)
        address = '127.0.0.1'
        port = 7777
        bind_socket(a_socket, address, port)
        self.assertEqual(a_socket.getsockname(), ('127.0.0.1', 7777))
        a_socket.close()


    def test_accept_connestion_socket(self):
        socket_server = socket(AF_INET, SOCK_STREAM)
        socket_client = socket(AF_INET, SOCK_STREAM)
        address = '127.0.0.1'
        port = 7777
        socket_server.bind((address, port))
        socket_server.listen(1)
        socket_client.connect((address, port))
        client, addr = accept_connestion_socket(socket_server)
        self.assertEqual(type(client), type(socket_server))
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
        socket_client.send(msg)
        bytes_num = 10000
        data = get_data(client, bytes_num)
        self.assertEqual(data, msg)
        socket_server.close()
        socket_client.close()
        client.close()

    
    def test_decode_and_load_bytes_correct(self):
        a_dict = {
        "action": "presence",
        "time": "Wed Apr 12 00:16:19 2023",
        "type": "status",
        "user": {
            "status": "Yep, I am here!"
            }
        }
        a_dict_dumped_encoded = b'{"action": "presence", "time": "Wed Apr 12 00:16:19 2023", "type": "status", "user": {"status": "Yep, I am here!"}}'
        self.assertEqual(decode_and_load_bytes(a_dict_dumped_encoded), a_dict)


    def test_decode_and_load_bytes_incorrect(self):
        encoded_message = b'Hello'
        self.assertRaises(json.decoder.JSONDecodeError, decode_and_load_bytes, encoded_message)


    def test_encode_and_dump_dict(self):
        a_dict = a_dict = {
        "action": "presence",
        "time": "Wed Apr 12 00:16:19 2023",
        "type": "status",
        "user": {
            "status": "Yep, I am here!"
            }
        }
        a_dict_dumped_encoded = b'{"action": "presence", "time": "Wed Apr 12 00:16:19 2023", "type": "status", "user": {"status": "Yep, I am here!"}}'
        self.assertEqual(encode_and_dump_dict(a_dict), a_dict_dumped_encoded)


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
        send_data(client, msg)
        received_msg = socket_client.recv(1024)
        self.assertEqual(msg, received_msg)
        socket_server.close()
        socket_client.close()
        client.close()


if __name__ == '__main__':
    unittest.main()
