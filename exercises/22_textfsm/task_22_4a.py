# -*- coding: utf-8 -*-
'''
Задание 22.4a

Переделать функцию из задания 22.4:
* добавить аргумент show_output, который контролирует будет ли выводится результат обработки команды на стандартный поток вывода
 * по умолчанию False, что значит результат не будет выводиться
* результат должен отображаться с помощью FormattedTable (пример есть в разделе)

'''
import clitable

def parse_command_dynamic(attr, output, index='index', tmpl_dir='templates', show_output=False):
    result = []
    temp_dict = {}
    cli_table = clitable.CliTable(index, tmpl_dir)
    cli_table.ParseCmd(output, attr)

    header = list(cli_table.header)
    data_rows = [list(row) for row in cli_table]

    for i in range(len(data_rows)):
        for j in range(len(header)):
            temp_dict[header[j]] = data_rows[i][j]
        result.append(temp_dict.copy())

    if show_output:
        print(cli_table.FormattedTable())
    return result

if __name__ == '__main__':
    output = open('output/sh_ip_int_br.txt').read()
    attributes = {'Command': 'sh ip int br', 'Vendor': 'cisco_ios'}
    parse_command_dynamic(attributes, output, show_output=True)