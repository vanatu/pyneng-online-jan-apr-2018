# -*- coding: utf-8 -*-
'''
Задание 21.3a

Измените шаблон templates/ospf.txt таким образом, чтобы для перечисленных переменных
были указаны значения по умолчанию, которые используются в том случае,
если переменная не задана.

Не использовать для этого выражения if/else.

Задать в шаблоне значения по умолчанию для таких переменных:
* process - значение по умолчанию 1
* ref_bw - значение по умолчанию 10000


Проверьте получившийся шаблон templates/ospf.txt, на данных в файле data_files/ospf2.yml,
с помощью функции generate_cfg_from_template из задания 21.1-21.1c.
Не копируйте код функции.

'''
from task_21_1c import generate_cfg_from_template

print(generate_cfg_from_template('templates/ospf.txt', 'data_files/ospf2.yml'))