# -*- coding: utf-8 -*-
'''
Задание 18.1a

Скопировать скрипт add_data.py из задания 18.1.

Добавить в файл add_data.py проверку на наличие БД:
* если файл БД есть, записать данные
* если файла БД нет, вывести сообщение, что БД нет и её необходимо сначала создать

'''

import glob, sqlite3, yaml, re, os

db_filename = 'dhcp_snooping.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')

db_exists = os.path.exists(db_filename)

def add_data_sw():
    with sqlite3.connect(db_filename) as conn:
        sw_file = 'switches.yml'
        query = 'insert into switches (hostname, location) values (?, ?)'

        with open(sw_file) as f:
            sw_info = yaml.load(f)

        for k,v in sw_info['switches'].items():
            try:
                with conn:
                    conn.execute(query, (k,v))
            except sqlite3.IntegrityError as e:
                print('Error occured: ', e)

def add_data_dhcp():
    with sqlite3.connect(db_filename) as conn:
        query = 'insert into dhcp (mac, ip, vlan, interface, switch) values (?, ?, ?, ?, ?)'
        result = []
        regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')

        for file in dhcp_snoop_files:
            hostname = re.match('(\S+?)_.*', file).group(1)
            with open(file) as f:
                for line in f:
                    match = regex.match(line)
                    if match:
                        result.append(match.groups() + (hostname,))

        for row in result:
            try:
                with conn:
                    conn.execute(query, row)
            except sqlite3.IntegrityError as e:
                print('Error occured: ', e)

if db_exists:
    add_data_sw()
    add_data_dhcp()
else:
    print('Need to create database -', db_filename)
