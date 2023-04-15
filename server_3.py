from socket import *
import time
import json
import argparse
from log import server_log_config

def write_log(func):
    def wrapper(*args, **kwargs):
        server_log_config.log.debug(f'Server module function {func.__name__} called')
        return func(*args, **kwargs)
    return wrapper


@write_log
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p',
        dest='port',
        type=int,
        default=7777,
        help='port (default: 7777)'
    )
    parser.add_argument(
        '-a',
        dest='address',
        type=str,
        default='',
        help='ip-address for listening (default: all addresses)'
    )
    return parser.parse_args()


@write_log
def init_tcp_socket():
    return socket(AF_INET, SOCK_STREAM)


@write_log
def bind_socket(a_sock, address, port):
    a_sock.bind((address, port))


@write_log
def accept_connestion_socket(a_sock):
    return a_sock.accept()


@write_log
def get_data(a_sock, bytes_num):
    return a_sock.recv(bytes_num)


@write_log
def decode_and_load_bytes(bytes):
    return json.loads(bytes.decode('utf-8'))


@write_log
def encode_and_dump_dict(dict):
    return json.dumps(dict).encode('utf-8')


@write_log
def send_data(a_sock, data):
    return a_sock.send(data)


@write_log
def main():
    args = get_args()
    s = init_tcp_socket()
    bind_socket(s, args.address, args.port)
    s.listen(5)
    while True:
        client, addr = accept_connestion_socket(s)
        data = get_data(client, 10000)
        response_code = 200
        try:
            server_log_config.log.debug('Try/except clause expired')
            data_decoded_json = decode_and_load_bytes(data)
            server_log_config.log.info(f'Было получено сообщение: {json.dumps(data_decoded_json)}')
            alert_msg = "Welcome, client!"
        except json.decoder.JSONDecodeError:
            response_code = 400
            alert_msg = "Bad Request"
            server_log_config.log.info('JSONDecodeError')

        response_msg = {
            "response": response_code,
            "time": time.ctime(time.time()),
            "alert": alert_msg
        }
        response_msg_encoded_json = encode_and_dump_dict(response_msg)
        send_data(client, response_msg_encoded_json)

        client.close()


if __name__ == '__main__':
    main()
