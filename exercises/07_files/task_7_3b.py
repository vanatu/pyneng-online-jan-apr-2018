# -*- coding: utf-8 -*-
'''
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Дополнить скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
with open('CAM_table.txt') as f:
    vlan = input('VLAN: ')
    for line in f:
        list_l = line.split()
        if len(list_l) == 4 and list_l[0] == vlan:
            print('{}    {}   {}'.format(list_l[0], list_l[1], list_l[3]))
