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
        print('Active values:')
        active_table = conn.execute('select * from dhcp where active=1')
        print(tabulate(active_table.fetchall()))

        print('Inactive values:')
        passive_table = conn.execute('select * from dhcp where active=0')
        print(tabulate(passive_table.fetchall()))
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

    active_query = 'select * from dhcp where {} = ? and active=1'.format( key )
    active_result = conn.execute(active_query, (value,))

    for row in active_result:
        for k in keys:
            print('{:12}: {}'.format(k, row[k]))
        print('-' * 40)

    passive_query = 'select * from dhcp where {} = ? and active=0'.format( key )
    passive_result = conn.execute(passive_query, (value,))

    print('\nInactive values:')

    for row in passive_result:
        for k in keys:
            print('{:12}: {}'.format(k, row[k]))
        print('-' * 40)

get_data()
