# -*- coding: utf-8 -*-
'''
Задание 19.1a

Переделать функцию send_show_command из задания 19.1 таким образом,
чтобы обрабатывалось исключение, которое генерируется
при ошибке аутентификации на устройстве.

При возникновении ошибки, должно выводиться сообщение исключения.

Для проверки измените пароль на устройстве или в файле devices.yaml.
'''
import netmiko, yaml
from pprint import pprint

command = 'show version | except \['

def send_show_command(device, command):
    result = {}
    with open(device) as f:
        devices = yaml.load(f)
        for d in devices['routers']:
            try:
                conn = netmiko.ConnectHandler(**d)
                output = conn.send_command(command)
                result[d['ip']] = output
            except netmiko.ssh_exception.NetMikoAuthenticationException:
                print('Not connect to {}. Authentication failed'.format(d['ip']))
    return result


if __name__ == '__main__':
    pprint(send_show_command('devices.yaml', command))