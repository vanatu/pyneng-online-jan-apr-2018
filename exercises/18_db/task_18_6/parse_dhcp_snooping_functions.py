#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3, os, glob
from datetime import timedelta, datetime

now = datetime.today().replace(microsecond=0)
week_ago = str(now - timedelta(days=7))

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




def add_data_switches():
    db_exists = os.path.exists(db_filename)
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

def add_data():
    dhcp_snoop_files = glob.glob('sw*_dhcp_snooping.txt')
    with sqlite3.connect(db_filename) as conn:
        query = 'replace into dhcp (mac, ip, vlan, interface, switch, last_active, active) values (?, ?, ?, ?, ?, ?, 1)'
        result = []
        regex = re.compile('(\S+) +(\S+) +\d+ +\S+ +(\d+) +(\S+)')

        for file in dhcp_snoop_files:
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

'''
# Default values:
DFLT_DB_NAME = 'dhcp_snooping.db'
DFLT_DB_SCHEMA = 'dhcp_snooping_schema.sql'


def create(args):
    print('Creating DB {} with DB schema {}'.format(args.name, args.schema))
    pds.create_db(args.name, args.schema)


def add(args):
    if args.sw_true:
        print('Adding switch data to database')
        pds.add_data_switches(args.db_file, args.filename)
    else:
        print('Reading info from file(s) \n{}'.format(', '.join(
            args.filename)))
        print('\nAdding data to db {}'.format(args.db_file))
        pds.add_data(args.db_file, args.filename)


def get(args):
    if args.key and args.value:
        print('Geting data from DB: {}'.format(args.db_file))
        print('Request data for host(s) with {} {}'.format(
            args.key, args.value))
        pds.get_data(args.db_file, args.key, args.value)
    elif args.key or args.value:
        print('Please give two or zero args\n')
        print(show_subparser_help('get'))
    else:
        print('Showing {} content...'.format(args.db_file))
        pds.get_all_data(args.db_file)


def show_subparser_help(subparser_name):
    \'''
    Function returns help message for subparser
    \'''
    subparsers_actions = [
        action for action in parser._actions
        if isinstance(action, argparse._SubParsersAction)
    ]
    return subparsers_actions[0].choices[subparser_name].format_help()


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(
    title='subcommands',
    description='valid subcommands',
    help='additional info')

create_parser = subparsers.add_parser('create_db', help='create new db')
create_parser.add_argument(
    '-n', dest='name', default=DFLT_DB_NAME, help='db filename')
create_parser.add_argument(
    '-s', dest='schema', default=DFLT_DB_SCHEMA, help='db schema filename')
create_parser.set_defaults(func=create)

add_parser = subparsers.add_parser('add', help='add data to db')
add_parser.add_argument('filename', nargs='+', help='file(s) to add to db')
add_parser.add_argument(
    '--db', dest='db_file', default=DFLT_DB_NAME, help='db name')
add_parser.add_argument(
    '-s',
    dest='sw_true',
    action='store_true',
    help='add switch data if set, else add normal data')
add_parser.set_defaults(func=add)

get_parser = subparsers.add_parser('get', help='get data from db')
get_parser.add_argument(
    '--db', dest='db_file', default=DFLT_DB_NAME, help='db name')
get_parser.add_argument(
    '-k',
    dest='key',
    choices=['mac', 'ip', 'vlan', 'interface', 'switch'],
    help='host key (parameter) to search')
get_parser.add_argument('-v', dest='value', help='value of key')
get_parser.add_argument('-a', action='store_true', help='show db content')
get_parser.set_defaults(func=get)

if __name__ == '__main__':
    args = parser.parse_args()
    if not vars(args):
        parser.print_usage()
    else:
        args.func(args)
'''