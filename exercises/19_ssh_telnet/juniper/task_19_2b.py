# -*- coding: utf-8 -*-
'''
Задание 19.2b

В этом задании необходимо переделать функцию send_config_commands из задания 19.2a или 19.2
и добавить проверку на ошибки.

При выполнении каждой команды, скрипт должен проверять результат на такие ошибки:
 * syntax error, missing argument, invalid interface type in 

Если при выполнении какой-то из команд возникла ошибка,
функция должна выводить сообщение на стандартный поток вывода с информацией
о том, какая ошибка возникла, при выполнении какой команды и на каком устройстве.

При этом, параметр verbose также должен работать, но теперь он отвечает за вывод
только тех команд, которые выполнились корректно.

Функция send_config_commands теперь должна возвращать кортеж из двух словарей:
* первый словарь с выводом команд, которые выполнились без ошибки
* второй словарь с выводом команд, которые выполнились с ошибками

Оба словаря в формате:
* ключ - команда
* значение - вывод с выполнением команд

Отправить список команд commands на все устройства из файла devices.yaml (для этого надо считать информацию из файла) с помощью функции send_config_commands.

Примеры команд с ошибками:
m120-lab# set 
                ^
syntax error.

m120-lab# set interfaces 
                          ^
missing argument.

m120-lab# set interfaces sdfsdf 
                                 ^
invalid interface type in 'sdfsdf'.

В файле задания заготовлены команды с ошибками и без:
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
            elif 'missing argument' in output:
                print('''Command "{}" error!
{}
'''.format(c, output)[:-23])
            elif 'invalid interface type in' in output:
                print('''Command "{}" error!
{}
'''.format(c, output)[:-23])

        net_connect.send_config_set("show | compare", exit_config_mode=False)
        net_connect.commit(and_quit=True)
    
    net_connect.disconnect()

if __name__ == '__main__':
    send_config_command(DEVICE, commands)