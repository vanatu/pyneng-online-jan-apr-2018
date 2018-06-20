# -*- coding: utf-8 -*-
import glob, sqlite3, yaml, re, os

db_filename = 'dhcp_snooping.db'
dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')

db_exists = os.path.exists(db_filename)

def add_data_sw():
    with sqlite3.connect(db_filename) as conn:
        sw_file = 'switches.yml'
        query = 'replace into switches (hostname, location) values (?, ?)'

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
        query = 'replace into dhcp (mac, ip, vlan, interface, switch, active) values (?, ?, ?, ?, ?, 1)'
        result = []
        regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')

        for file in dhcp_snoop_files:
            hostname = re.match('(\S+?)_.*', file).group(1)
            with open(file) as f:
                for line in f:
                    match = regex.match(line)
                    if match:
                        result.append(match.groups() + (hostname,))

        query_active = 'update dhcp set active=0'
        conn.execute(query_active)
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
