# -*- coding: utf-8 -*-
'''
Задание 15.3a

Переделать функцию parse_cfg из задания 15.3 таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
import re
from pprint import pprint

def parse_cfg(file):
    regex = re.compile('interface (?P<intf>\S+)'
                       '| ip address (?P<ip>\S+) (?P<mask>\S+)')
    result = {}
    with open(file) as f:
        matches = regex.finditer(f.read())
        for match in matches:
            if match.lastgroup == 'intf':
                intf = match.group(match.lastgroup)
            elif match.lastgroup == 'mask':
                result[intf] = (match.group('ip'), match.group('mask'))

    return result

if __name__ == '__main__':
    pprint(parse_cfg('config_r1.txt'))
