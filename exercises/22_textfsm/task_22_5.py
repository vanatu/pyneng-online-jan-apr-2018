# -*- coding: utf-8 -*-
'''
Задание 22.5

В этом задании соединяется функциональность TextFSM и подключение к оборудованию.

Задача такая:
* подключиться к оборудованию
* выполнить команду show
* полученный вывод передавать на обработку TextFSM
* вернуть результат обработки

Для этого, воспользуемся функциями, которые были созданы ранее:
* функцией send_show_command из упражнения 19.1
* функцией parse_command_dynamic из упражнения 22.4

В этом упражнении нужно создать функцию send_and_parse_command:
* функция должна использовать внутри себя функции parse_command_dynamic и send_show_command.
* какие аргументы должны быть у функции send_and_parse_command, нужно решить самостоятельно
 * но, надо иметь в виду, какие аргументы ожидают две готовые функции, которые мы используем
* функция send_and_parse_command должна возвращать:
 * функция send_show_command возвращает словарь с результатами выполнения команды:
    * ключ - IP устройства
    * значение - результат выполнения команды
 * затем, нужно отправить полученный вывод на обработку функции parse_command_dynamic
 * в результате, должен получиться словарь, в котором:
    * ключ - IP устройства
    * значение - список словарей (то есть, тот вывод, который был получен из функции parse_command_dynamic)

Для функции send_show_command создан файл devices.yaml, в котором находятся параметры подключения к устройствам.

Проверить работу функции send_and_parse_command на команде sh ip int br.
'''
import sys
sys.path.append('/home/vanatu/pyneng-online-jan-apr-2018/exercises/19_ssh_telnet/juniper')
from task_19_1 import send_show_command
from task_22_4 import parse_command_dynamic

def send_and_parse_command(devices, command):
    result = {}
    attr = {'Command': command}
    output = send_show_command(devices, command)
    for ip, out in output.items():
        result[ip] = parse_command_dynamic(attr, out, tmpl_dir='templates_jun')
    return result


if __name__ == '__main__':
    command = 'show version'
    print(send_and_parse_command('devices_jun.yaml', command))
