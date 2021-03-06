# -*- coding: utf-8 -*-
'''
Задание 17.2

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa0/1': {'R5': 'Fa0/1'},
        'Fa0/2': {'R6': 'Fa0/0'}}}

При этом интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
'''
import re
from pprint import pprint

def parse_sh_cdp_neighbors(output):
    result = {}
    regex = re.compile('(?P<hostname>\S+)>show cdp neighbors'
                        '|(?P<nbr>\S+) +(?P<lintf>\w+\s?\d/\d+)'
                        '.*?(?P<rintf>\w+\s?\d/\d+)')

    match_iter = regex.finditer(output)

    for match in match_iter:
        if match.lastgroup == 'hostname':
            hostname = match.group(match.lastgroup)
            result[hostname] = {}
        elif match.lastgroup == 'rintf':
            lintf = match.group('lintf')
            nbr = match.group('nbr')
            rintf = match.group('rintf')
            result[hostname][lintf] = {nbr:rintf}

    return result

if __name__ == '__main__':
    with open('sh_cdp_n_sw1.txt') as f:
        pprint(parse_sh_cdp_neighbors(f.read()))
