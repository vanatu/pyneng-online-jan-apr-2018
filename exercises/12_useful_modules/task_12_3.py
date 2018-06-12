# -*- coding: utf-8 -*-
'''
Задание 12.3


Создать функцию ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые передавны ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.

'''
from tabulate import tabulate

def ip_table(ip_ok, ip_bad):
    strings = []
    col = ['Reachable', 'Unreachable']
    max_len = max(len(ip_ok), len(ip_bad))
    if len(ip_ok) < max_len:
        ip_ok += ['']*(max_len - len(ip_ok))
    else:
        ip_bad += ['']*(max_len - len(ip_bad))

    for i in range(max_len):
        strings.append((ip_ok[i], ip_bad[i]))

    return tabulate(strings, headers = col)

if __name__ == '__main__':
    print(ip_table(['8.8.8.8', '8.8.4.4'], ['8.8.8.9', '1.1.1.1', '2.2.2.2', '3.3.3.3']))
