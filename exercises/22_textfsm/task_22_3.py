# -*- coding: utf-8 -*-
'''
Задание 22.3

Сделать шаблон TextFSM для обработки вывода sh ip dhcp snooping binding.
Вывод команды находится в файле output/sh_ip_dhcp_snooping.txt.

Шаблон должен обрабатывать и возвращать значения таких столбцов:
* MacAddress
* IpAddress
* VLAN
* Interface

Проверить работу шаблона с помощью функции из задания 22.1.
'''
from task_22_1 import parse_output
from pprint import pprint

output = open('output/sh_ip_dhcp_snooping.txt').read()
pprint(parse_output('templates/sh_ip_dhcp_snooping.template', output))
