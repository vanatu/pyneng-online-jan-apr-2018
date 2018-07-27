# -*- coding: utf-8 -*-
'''
Задание 20.2

Создать функцию send_commands_threads, которая запускает функцию send_commands из задания 19.3
 на разных устройствах в параллельных потоках.

Параметры функции send_commands_threads надо определить самостоятельно.
Должна быть возможность передавать параметры show, config, filename функции send_commands.

Функция send_commands_threads возвращает словарь с результатами выполнения команд на устройствах:

* ключ - IP устройства
* значение - вывод с выполнением команд

'''
import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed

ip = ['8.8.8.8', '8.8.4.4', '128.0.0.10', '40.20.10.1']

start = datetime.datetime.now()


def check_ip_addresses(ip, hello=False):
	ip_ok, ip_bad = [], []
	if hello:
		print('print {}'.format(ip).center(20, '#'))
	r = subprocess.run('ping -n 3 {}'.format(ip),
		 					shell = True,
							#stdout=subprocess.DEVNULL
							)
	ip_ok.append(ip) if r.returncode == 0 else ip_bad.append(ip)
	
	return ip_ok, ip_bad

def threads_ping(function, ip, limit=1):
    all_results = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        f_result = [executor.submit(function, i, hello=True) for i in ip]
    for f in as_completed(f_result):
        all_results.append(f.result())
    
    return all_results

print(threads_ping(check_ip_addresses, ip, 4))


print(datetime.datetime.now() - start)