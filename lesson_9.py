'''
1. Написать функцию host_ping(), в которой с помощью утилиты ping будет
проверяться доступность сетевых узлов. Аргументом функции является список,
в котором каждый сетевой узел должен быть представлен именем хоста или
ip-адресом. В функции необходимо перебирать ip-адреса и проверять их
доступность с выводом соответствующего сообщения («Узел доступен», «Узел
недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью
функции ip_address().
'''


import ipaddress
import subprocess


addresses = ['127.0.0.1', '192.158.1.48', '130.80.80.99', '255.255.255.255', 'mail.ru']
ip_addresses = map(ipaddress.ip_address, addresses)


def host_ping(ip_list):
    for ip in ip_list:
        try:
            ip = ipaddress.ip_address(ip)
        except ValueError:
            pass
        if subprocess.call(f'ping {ip}') == 0:
            print(f'Узел {ip} доступен')
        else:
            print(f'Узел {ip} не доступен')


'''
2. Написать функцию host_range_ping() для перебора ip-адресов из
заданного диапазона. Меняться должен только последний октет каждого
адреса. По результатам проверки должно выводиться соответствующее сообщение.
'''


an_addr_range = ('127.0.0.1', '127.0.0.3')


def host_range_ping(addr_range: tuple):
    start_val = int(addr_range[0].split('.')[3])
    base = '.'.join(addr_range[0].split('.')[:-1])
    end_val = int(addr_range[1].split('.')[3])
    for ip_addr in range(start_val, end_val+1):
        ip_addr = base + '.' + str(ip_addr)
        ip_addr = ipaddress.ip_address(ip_addr)
        if subprocess.call(f'ping {ip_addr}') == 0:
            print(f'Узел {ip_addr} доступен')
        else:
            print(f'Узел {ip_addr} не доступен')


'''
3. Написать функцию host_range_ping_tab(), возможности которой основаны
на функции из примера 2. Но в данном случае результат должен быть итоговым
по всем ip-адресам, представленным в табличном формате (использовать модуль
tabulate).
'''


from tabulate import tabulate


def host_range_ping_tab(addr_range: tuple):
    start_val = int(addr_range[0].split('.')[3])
    base = '.'.join(addr_range[0].split('.')[:-1])
    end_val = int(addr_range[1].split('.')[3])
    ping_results = []
    for ip_addr in range(start_val, end_val+1):
        ip_addr = base + '.' + str(ip_addr)
        ip_addr = ipaddress.ip_address(ip_addr)
        if subprocess.call(f'ping {ip_addr}') == 0:
            ping_results.append({'Reachable': ip_addr})

        else:
            ping_results.append({'Unreachable': ip_addr})
    print(tabulate(ping_results, headers='keys'))


if __name__ == '__main__':
    host_ping(addresses)
    host_range_ping(an_addr_range)
    host_range_ping_tab(an_addr_range)
