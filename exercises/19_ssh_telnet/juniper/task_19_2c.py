# -*- coding: utf-8 -*-
'''
Задание 19.2c

Переделать функцию send_config_commands из задания 19.2b

Если при выполнении команды возникла ошибка,
спросить пользователя надо ли выполнять остальные команды.

Варианты ответа [y]/n:
* y - выполнять остальные команды (значение по умолчанию)
* n - не выполнять остальные команды

Функция send_config_commands по-прежнему должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками


Оба словаря в формате
* ключ - команда
* значение - вывод с выполнением команд

Проверить функцию на командах с ошибкой.

'''
commands_with_errors = ['set', 'set interfaces', 'set interfaces sdfsdf']
correct_commands = [
    'set routing-instances v1998-TEST instance-type virtual-router',
    'set routing-instances v1998-TEST description "1"'
    ]

commands = commands_with_errors + correct_commands

from netmiko import Netmiko

DEVICE = {
    'device_type': 'juniper',
    'ip': '10.251.15.251',
    'username': 'lab',
    'password': 'lab123',
    'verbose': True,
}

def exit_or_continue():
    answer = input('''Выполнять остальные команды?
Варианты ответа [y]/n:
* y - выполнять остальные команды (значение по умолчанию)
* n - не выполнять остальные команды
: ''')
    if answer == 'n':
        return True


def send_config_command(device, config_commands):
    net_connect = Netmiko(**device)
    net_connect.find_prompt()
    net_connect.config_mode(config_command='configure private')
    if net_connect.check_config_mode():
        for c in config_commands:
            output = net_connect.send_config_set(c, exit_config_mode=False)
            if 'syntax error' in output:
                print('''Command "{}" error!
{}
'''.format(c, output)[:-23])
                if exit_or_continue():
                    break
            elif 'missing argument' in output:
                print('''Command "{}" error!
{}
'''.format(c, output)[:-23])
                if exit_or_continue():
                    break
            elif 'invalid interface type in' in output:
                print('''Command "{}" error!
{}
'''.format(c, output)[:-23])
                if exit_or_continue():
                    break

        net_connect.send_config_set("show | compare", exit_config_mode=False)
        net_connect.commit(and_quit=True)
    
    net_connect.disconnect()

if __name__ == '__main__':
    send_config_command(DEVICE, commands)