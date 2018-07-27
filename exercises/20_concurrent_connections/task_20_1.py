# -*- coding: utf-8 -*-
'''
Задание 20.1

Переделать задание 19.4a таким образом, чтобы проверка доступности устройств
выполнялась не последовательно, а параллельно.

Для этого, можно взять за основу функцию check_ip_addresses из задания 12.1.
Функцию надо переделать таким образом, чтобы проверка IP-адресов выполнялась
параллельно в разных потоках.

'''
import sys, datetime
sys.path.append('X:\python_apps\pyneng-online-jan-apr-2018\exercises\\12_useful_modules\\')
from task_12_1 import check_ip_addresses
from concurrent.futures import ThreadPoolExecutor

ip = ['8.8.8.8', '8.8.4.4', '128.0.0.10', '40.20.10.1']

start = datetime.datetime.now()

def threads_ping(function, ip, limit=1):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        f_result = executor.map(function, ip)
    return list(f_result)

print(threads_ping(check_ip_addresses, ip, 8))


print(datetime.datetime.now() - start)