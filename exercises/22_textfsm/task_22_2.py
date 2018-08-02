# -*- coding: utf-8 -*-
'''
Задание 22.2

В этом задании нужно использовать функцию parse_output из задания 22.1.
Она используется для того, чтобы получить структурированный вывод
в результате обработки вывода команды.

Полученный вывод нужно записать в CSV формате.

Для записи вывода в CSV, нужно создать функцию list_to_csv, которая ожидает как аргументы:
* список:
 * первый элемент - это список с названиями заголовков
 * остальные элементы это списки, в котором находятся результаты обработки вывода
* имя файла, в который нужно записать данные в CSV формате

Проверить работу функции на примере обработки
команды sh ip int br (шаблон и вывод есть в разделе).
'''

from task_22_1 import parse_output
import csv

def list_to_csv(data_list, csv_file_out):
    with open(csv_file_out, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        for row in data_list:
            writer.writerow(row)

if __name__ == '__main__':
    output = open('output/sh_ip_int_br.txt').read()
    list_to_csv(parse_output('templates/sh_ip_int_br.template', output), 'task_22_2.csv')