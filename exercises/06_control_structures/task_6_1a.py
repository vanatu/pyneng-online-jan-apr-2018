# -*- coding: utf-8 -*-
'''
Задание 6.1a

Сделать копию скрипта задания 6.1.

Дополнить скрипт:
- Добавить проверку введенного IP-адреса.
- Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой,
   - каждое число в диапазоне от 0 до 255.

Если адрес задан неправильно, выводить сообщение:
'Incorrect IPv4 address'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
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
else:
    print('Incorrect IPv4 address')