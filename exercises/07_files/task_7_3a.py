# -*- coding: utf-8 -*-
'''
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN


Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
with open('CAM_table.txt') as f:
    result = []
    for line in f:
        list_l = line.split()
        if len(list_l) == 4 and list_l[0].isdigit():
            result += ['{}    {}   {}'.format(list_l[0], list_l[1], list_l[3])]

    for i in sorted(result):
        print(i)
