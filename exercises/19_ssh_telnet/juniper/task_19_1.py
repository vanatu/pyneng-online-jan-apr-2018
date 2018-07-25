# -*- coding: utf-8 -*-
'''
Задание 19.1

Создать функцию send_show_command.

Функция подключается по SSH (с помощью netmiko) к устройству и выполняет указанную команду.

Параметры функции:
* device - словарь с параметрами подключения к устройству
* command - команда, которую надо выполнить

Функция возвращает словарь с результатами выполнения команды:
* ключ - IP устройства
* значение - результат выполнения команды

Отправить команду command на все устройства из файла devices.yaml (для этого надо считать информацию из файла)
с помощью функции send_show_command.

'''
import netmiko, yaml
from pprint import pprint

command = 'show version | except \['

def send_show_command(device, command):
    result = {}
    with open(device) as f:
        devices = yaml.load(f)
        for d in devices['routers']:
            conn = netmiko.ConnectHandler(**d)
            output = conn.send_command(command)
            result[d['ip']] = output
    return result


if __name__ == '__main__':
    pprint(send_show_command('devices.yaml', command))