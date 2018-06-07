# -*- coding: utf-8 -*-
'''
Задание 9.4a

Задача такая же, как и задании 9.4.
Проверить работу функции надо на примере файла config_r1.txt

Обратите внимание на конфигурационный файл.
В нем есть разделы с большей вложенностью, например, разделы:
* interface Ethernet0/3.100
* router bgp 100

Надо чтобы функция config_to_dict обрабатывала следующий уровень вложенности.
При этом, не привязываясь к конкретным разделам.
Она должна быть универсальной, и сработать, если это будут другие разделы.

Если уровня вложенности два:
* то команды верхнего уровня будут ключами словаря,
* а команды подуровней - списками

Если уровня вложенности три:
* самый вложенный уровень должен быть списком,
* а остальные - словарями.

На примере interface Ethernet0/3.100:

{'interface Ethernet0/3.100':{
               'encapsulation dot1Q 100':[],
               'xconnect 10.2.2.2 12100 encapsulation mpls':
                   ['backup peer 10.4.4.4 14100',
                    'backup delay 1 1']}}


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from pprint import pprint

ignore = ['duplex', 'alias', 'Current configuration']


def check_ignore(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает True, если в команде содержится слово из списка ignore, False - если нет

    '''
    return any(word in command for word in ignore)

def config_to_dict(config_file):
    result = {}
    with open(config_file) as f:
        item_list = [line.rstrip() for line in f.read().split('\n')
            if line and not ('!' in line or check_ignore(line, ignore))]
        for item in item_list:
            if not item.startswith(' '):
                key = item
                result[key] = []
            else:
                result[key].append(item)

    for k,v in result.items():
        if any([i.startswith('  ') for i in v]):
            result[k] = {}
            for j in v:
                if not j.startswith('  '):
                    key2 = j
                    result[k][key2] = []
                else:
                    result[k][key2].append(j)

    return result

pprint(config_to_dict('config_r1.txt'))
