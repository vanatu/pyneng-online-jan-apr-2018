# -*- coding: utf-8 -*-
'''
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой.

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {('R4', 'Fa0/1'): ('R5', 'Fa0/1'),
     ('R4', 'Fa0/2'): ('R6', 'Fa0/0')}

Интерфейсы могут быть записаны с пробелом Fa 0/0 или без Fa0/0.

Проверить работу функции на содержимом файла sw1_sh_cdp_neighbors.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
from pprint import pprint

def parse_cdp_neighbors(file):
    result = {}
    with open(file) as f:
        for line in [i for i in f.read().split('\n') if i]:
            if line.endswith('show cdp neighbors'):
                local_dev = line.split('>')[0]
            elif line[-1].isdigit():
                rem_dev, local_media, local_port, *_, rem_media, rem_port = line.split()
                result[(local_dev, local_media + local_port)] = (rem_dev, rem_media + rem_port)

    return result

if __name__ == '__main__':
    pprint(parse_cdp_neighbors('sh_cdp_n_r2.txt'))
