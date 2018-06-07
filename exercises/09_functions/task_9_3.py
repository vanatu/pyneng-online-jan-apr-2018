# -*- coding: utf-8 -*-
'''
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает два объекта:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN:
{'FastEthernet0/12':10,
 'FastEthernet0/14':11,
 'FastEthernet0/16':17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN:
{'FastEthernet0/1':[10,20],
 'FastEthernet0/2':[11,30],
 'FastEthernet0/4':[17]}

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
from pprint import pprint

def get_int_vlan_map(cfg_file):
    access, trunk = {},{}
    with open(cfg_file) as f:
        intf = ''
        for line in f:
            line = line.rstrip()
            if line.startswith('interface'):
                intf = line.split()[1]
            if 'access vlan' in line:
                access[intf] = int(line.split('vlan ')[1])
            elif 'trunk allowed' in line:
                trunk[intf] = [int(vl) for vl in line.split('vlan ')[1].split(',')]

    return (access, trunk)

pprint(get_int_vlan_map('config_sw1.txt'))