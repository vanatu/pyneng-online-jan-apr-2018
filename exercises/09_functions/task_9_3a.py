# -*- coding: utf-8 -*-
'''
Задание 9.3a

Сделать копию скрипта задания 9.3.

Дополнить скрипт:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12':10,
                       'FastEthernet0/14':11,
                       'FastEthernet0/20':1 }

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


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

pprint(get_int_vlan_map('config_sw2.txt'))