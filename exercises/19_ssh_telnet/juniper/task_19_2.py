# -*- coding: utf-8 -*-
'''
Задание 19.2

Создать функцию send_config_commands

Функция подключается по SSH (с помощью netmiko) к устройству и выполняет перечень команд
в конфигурационном режиме
на основании переданных аргументов.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* config_commands - список команд, которые надо выполнить

Функция возвращает словарь с результатами выполнения команды:
* ключ - команда
* значение - вывод с выполнением команды

'''

commands = [
    'delete routing-instances v1998-TEST',
]

import netmiko

DEVICE = {
    'device_type': 'juniper',
    'ip': '10.251.15.251',
    'username': 'lab',
    'password': 'lab123',
    'verbose': False,
}

def send_config_command(device, config_commands):
    net_connect = netmiko.ConnectHandler(**device)
    print(net_connect.find_prompt())
    print(net_connect.config_mode(config_command='configure private'))
    if net_connect.check_config_mode():
        net_connect.send_config_set(config_commands, exit_config_mode=False)
        output = net_connect.send_config_set("show | compare", exit_config_mode=False)
        output += net_connect.commit(and_quit=True)
        print(output)
    
    net_connect.disconnect()

if __name__ == '__main__':
    send_config_command(DEVICE, commands)