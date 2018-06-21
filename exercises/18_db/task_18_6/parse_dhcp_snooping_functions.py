#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3, os, yaml, re, sys
from datetime import timedelta, datetime
from tabulate import tabulate


def create_db(name, schema):

  if not os.path.exists(name):
    conn = sqlite3.connect(name)
    print('Creating schema...')

    with open(schema) as f:
      conn.executescript(f.read())
      print('Done')

    conn.close()

  else:
    print('DB already exists')


def add_data_switches(db, sw_file):
    db_exists = os.path.exists(db)
    with sqlite3.connect(db) as conn:
        query = 'replace into switches (hostname, location) values (?, ?)'

        with open(sw_file[0]) as f:
            sw_info = yaml.load(f)

        for k,v in sw_info['switches'].items():
            try:
                with conn:
                    conn.execute(query, (k,v))
            except sqlite3.IntegrityError as e:
                print('Error occured: ', e)

def add_data(db, files):
    now = datetime.today().replace(microsecond=0)
    week_ago = str(now - timedelta(days=7))

    with sqlite3.connect(db) as conn:
        query = 'replace into dhcp (mac, ip, vlan, interface, switch, last_active, active) values (?, ?, ?, ?, ?, ?, 1)'
        result = []
        regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')

        for file in files:
            hostname = re.match('(\S+?)_.*', file).group(1)
            with open(file) as f:
                for line in f:
                    match = regex.match(line)
                    if match:
                        result.append(match.groups() + (hostname, now))

        query_active = 'update dhcp set active=0'
        conn.execute(query_active)
        for row in result:
            try:
                with conn:
                    conn.execute(query, row)
            except sqlite3.IntegrityError as e:
                print('Error occured: ', e)

        query_clear_old = 'delete from dhcp where last_active < ?'
        conn.execute(query_clear_old, (week_ago,))


def get_all_data(db):
    conn = sqlite3.connect(db)

    print('Active values:')
    active_table = conn.execute('select * from dhcp where active=1')
    print(tabulate(active_table.fetchall()))

    print('Inactive values:')
    passive_table = conn.execute('select * from dhcp where active=0')
    print(tabulate(passive_table.fetchall()))
    sys.exit()
    

def get_data(db, key, value):
    conn = sqlite3.connect(db)
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
