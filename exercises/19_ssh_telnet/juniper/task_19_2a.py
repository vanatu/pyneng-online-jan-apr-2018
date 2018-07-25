# -*- coding: utf-8 -*-
'''
Задание 19.2a

Дополнить функцию send_config_commands из задания 19.2

Добавить аргумент verbose, который контролирует будет ли результат
выполнения команд выводится на стандартный поток вывода.

По умолчанию, результат должен выводиться.
'''
commands = [
    'set routing-instances v1998-TEST instance-type virtual-router',
    'set routing-instances v1998-TEST description "1"',
]

from netmiko import Netmiko

DEVICE = {
    'device_type': 'juniper',
    'ip': '10.251.15.251',
    'username': 'lab',
    'password': 'lab123',
    'verbose': True,
}

def send_config_command(device, config_commands):
    net_connect = Netmiko(**device)
    output = net_connect.find_prompt()
    output += net_connect.config_mode(config_command='configure private')
    if net_connect.check_config_mode():
        output += net_connect.send_config_set(config_commands, exit_config_mode=False)
        output += net_connect.send_config_set("show | compare", exit_config_mode=False)
        output += net_connect.commit(and_quit=True)
        print(output)
    
    net_connect.disconnect()

if __name__ == '__main__':
    send_config_command(DEVICE, commands)