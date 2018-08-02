# -*- coding: utf-8 -*-
'''
Задание 22.6

Это задание похоже на задание 22.5, но в этом задании подключения надо выполнять параллельно с помощью потоков.
Для параллельного подключения использовать модуль concurrent.futures.

В этом упражнении нужно создать функцию send_and_parse_command_parallel:
* она должна использовать внутри себя функцию send_and_parse_command
* какие аргументы должны быть у функции send_and_parse_command_parallel, нужно решить самостоятельно
* функция send_and_parse_command_parallel должна возвращать словарь, в котором:
 * ключ - IP устройства
 * значение - список словарей

Проверить работу функции send_and_parse_command_parallel на команде sh ip int br.

'''

import yaml
from task_22_5 import send_and_parse_command
from concurrent.futures import ThreadPoolExecutor
from itertools import repeat

def send_and_parse_command_parallel(device, command, limit=2):
    device = [device] * limit
    with ThreadPoolExecutor(max_workers=limit) as executor:
        f_result = executor.map(send_and_parse_command, device, repeat(command))
    return list(f_result)


test_command = "show version"
devices = yaml.load(open('devices_jun.yaml'))

print(send_and_parse_command_parallel('devices_jun.yaml', test_command))
