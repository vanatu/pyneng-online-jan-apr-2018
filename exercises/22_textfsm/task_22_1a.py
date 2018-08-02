# -*- coding: utf-8 -*-
'''
Задание 22.1a

Переделать функцию parse_output из задания 22.1 таким образом,
чтобы, вместо списка списков, она возвращала один список словарей:
* ключи - названия столбцов,
* значения, соответствующие значения в столбцах.

То есть, для каждой строки будет один словарь в списке.
'''

import textfsm
from pprint import pprint

def parse_output(template, output):
    with open(template) as f:
        result = []
        temp_dict = {}
        re_table = textfsm.TextFSM(f)
        header = re_table.header
        match = re_table.ParseText(output)
        for i in range(len(match)):
            for j in range(len(header)):
                temp_dict[header[j]] = match[i][j]
            result.append(temp_dict.copy())
        return result


if __name__ == '__main__':
    output = open('output/sh_cdp_n_det.txt').read()
    pprint(parse_output('templates/sh_cdp_n_det.template', output))