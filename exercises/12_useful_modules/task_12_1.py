# -*- coding: utf-8 -*-
'''
Задание 12.1

Создать функцию check_ip_addresses, которая проверяет доступность IP-адресов.

Функция ожидает как аргумент список IP-адресов.
И возвращает два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте ping.
Адрес считается доступным, если на три ICMP-запроса пришли три ответа.

Ограничение: Все задания надо выполнять используя только пройденные темы.
'''
import subprocess
from pprint import pprint

def check_ip_addresses(ip_list):
	ip_ok, ip_bad = [], []
	for ip in ip_list:
		r = subprocess.run('ping -c 3 {}'.format(ip),
		 					shell = True,
							stdout=subprocess.DEVNULL)
		if r.returncode == 0:
			ip_ok.append(ip)
		else:
			ip_bad.append(ip)

	return ip_ok, ip_bad

if __name__ == '__main__':
	pprint(check_ip_addresses(['8.8.8.8', '8.8.4.4', '127.0.0.1', '40.20.10.1']))
