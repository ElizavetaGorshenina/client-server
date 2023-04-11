from socket import *
import time
import json
import argparse


def main():
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
    args = parser.parse_args()
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((args.addr, int(args.port[1:-1])))
    
    presence_msg = {
        "action": "presence",
        "time": time.ctime(time.time()),
        "type": "status",
        "user": {
            "status": "Yep, I am here!"
        }
    }
    presence_msg_json_encoded = json.dumps(presence_msg).encode('utf-8')
    s.send(presence_msg_json_encoded)
    server_msg = s.recv(1024)
    server_msg_decoded_json = json.loads(server_msg.decode('utf-8'))

    s.close()
    print('Сообщение от сервера:', server_msg_decoded_json)


if __name__ == '__main__':
    main()
