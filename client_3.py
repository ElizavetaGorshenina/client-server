from socket import *
import time
import argparse
from server_3 import init_tcp_socket, decode_and_load_bytes, encode_and_dump_dict, send_data, get_data
from log import client_log_config
import json
import inspect

def log(func):
    def wrapper(*args, **kwargs):
        frm = inspect.stack()[1]
        caller = frm[3]
        caller_file = frm[1].split("\\")[-1]
        client_log_config.log.debug(f'Вызов функции {func.__name__} с аргументами {args} {kwargs} из функции {caller} модуля {caller_file}')
        return func(*args, **kwargs)
    return wrapper


@log
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'addr',
        type=str,
        help='server ip address'
    )
    parser.add_argument(
        'port',
        type=str,
        help='server tcp-port as [<port>], please use [7777] by default'
    )
    return parser.parse_args()


@log
def connect_socket(a_sock, address, port):
    a_sock.connect((address, port))


def main():
    args = get_args()
    s = init_tcp_socket()
    connect_socket(s, args.addr, int(args.port[1:-1]))
    
    presence_msg = {
        "action": "presence",
        "time": time.ctime(time.time()),
        "type": "status",
        "user": {
            "status": "Yep, I am here!"
        }
    }
    presence_msg_json_encoded = encode_and_dump_dict(presence_msg)
    send_data(s, presence_msg_json_encoded)
    server_msg = get_data(s, 1024)
    server_msg_decoded_json = decode_and_load_bytes(server_msg)

    s.close()
    client_log_config.log.info(f'Сообщение от сервера: {json.dumps(server_msg_decoded_json)}')


if __name__ == '__main__':
    main()
