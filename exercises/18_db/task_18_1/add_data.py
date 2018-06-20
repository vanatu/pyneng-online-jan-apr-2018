# -*- coding: utf-8 -*-
'''
Задание 18.1

add_data.py
* с помощью этого скрипта, выполняется добавление данных в БД
* добавлять надо не только данные из вывода sh ip dhcp snooping binding,
   но и информацию о коммутаторах


В файле add_data.py должны быть две части:
* информация о коммутаторах добавляется в таблицу switches
 * данные о коммутаторах, находятся в файле switches.yml
* информация на основании вывода sh ip dhcp snooping binding добавляется в таблицу dhcp
 * вывод с трёх коммутаторов:
   * файлы sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt
 * так как таблица dhcp изменилась, и в ней теперь присутствует поле switch,
  его нужно также заполнять. Имя коммутатора определяется по имени файла с данными

Код должен быть разбит на функции.
Какие именно функции и как разделить код, надо решить самостоятельно.
Часть кода может быть глобальной.
'''

import glob, sqlite3, yaml, re

db_filename = 'dhcp_snooping.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')

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


add_data_sw()
add_data_dhcp()
