# -*- coding: utf-8 -*-
import sqlite3, sys
from tabulate import tabulate

db_filename = 'dhcp_snooping.db'

def get_data():
    if len(sys.argv) > 3:
        print('Пожалуйста, введите два или ноль аргументов')
        sys.exit()

    conn = sqlite3.connect(db_filename)

    if len(sys.argv) == 1:
        table = conn.execute('select * from dhcp')
        print(tabulate(table.fetchall()))
        sys.exit()

    key, value = sys.argv[1:]
    keys = ['mac', 'ip', 'vlan', 'interface', 'switch']
    if key not in keys:
        print('Данный параметр не поддерживается.\n'
              'Допустимые значения параметров: {}, {}, {}, {}, {}'.format(*keys))
        sys.exit()

    keys.remove(key)

    conn.row_factory = sqlite3.Row

    print('\nDetailed information for host(s) with', key, value)
    print('-' * 40)

    query = 'select * from dhcp where {} = ?'.format( key )
    result = conn.execute(query, (value,))

    for row in result:
        for k in keys:
            print('{:12}: {}'.format(k, row[k]))
        print('-' * 40)

get_data()
