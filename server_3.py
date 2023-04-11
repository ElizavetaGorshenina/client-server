from socket import *
import time
import json
import argparse

def main():
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
    args = parser.parse_args()
    s = socket(AF_INET, SOCK_STREAM)
    s.bind((args.address, args.port))
    s.listen(5)
    while True:
        client, addr = s.accept()
        data = client.recv(10000)
        response_code = 200
        try:
            data_decoded_json = json.loads(data.decode('utf-8'))
            print('Было получено сообщение:', data_decoded_json)
            alert_msg = "Welcome, client!"
        except json.decoder.JSONDecodeError:
            response_code = 400
            alert_msg = "Bad Request"
            print('JSONDecodeError')

        response_msg = {
            "response": response_code,
            "time": time.ctime(time.time()),
            "alert": alert_msg
        }
        response_msg_encoded_json = json.dumps(response_msg).encode('utf-8')
        client.send(response_msg_encoded_json)

        client.close()


if __name__ == '__main__':
    main()
