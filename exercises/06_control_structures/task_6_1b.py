# -*- coding: utf-8 -*-
'''
Задание 6.1b

Сделать копию скрипта задания 6.1a.

Дополнить скрипт:
Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
while True:
    ip = input('IP-address: ')
    if ip.count('.') == 3 and False not in [o.isdigit() and 0 <= int(o) <= 255 for o in ip.split('.')]:
        octs = [int(octet) for octet in ip.split('.')]
        if sum(octs) == 0:
            print('unassigned')
        elif sum(octs) == 255*4:
            print('local broadcast')
        elif octs[0] < 224:
            print('unicast')
        elif octs[0] < 240:
            print('multicast')
        else:
            print('unused')
        break
    else:
        print('Incorrect IPv4 address')