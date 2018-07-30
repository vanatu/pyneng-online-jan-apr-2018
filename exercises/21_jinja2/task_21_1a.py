# -*- coding: utf-8 -*-
'''
Задание 21.1a

Дополнить функцию generate_cfg_from_template из задания 21.1:

Функция generate_cfg_from_template должна принимать любые аргументы,
которые принимает класс Environment и просто передавать их ему.

То есть, надо добавить возможность контролировать аргументы trim_blocks, lstrip_blocks
и любые другие аргументы Environment через функцию generate_cfg_from_template.

Проверить функциональность на аргументах:
* trim_blocks
* lstrip_blocks

'''
from jinja2 import Environment, FileSystemLoader
import yaml, sys, os

def generate_cfg_from_template(path_template, path_vars_yaml, trim=True, lstrip=True):
    TEMPLATE_DIR, template_file = os.path.split(path_template)
    vars_dict = yaml.load(open(path_vars_yaml))

    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        trim_blocks=trim,
        lstrip_blocks=lstrip)
    template = env.get_template(template_file)

    return template.render(vars_dict)

print(generate_cfg_from_template('templates/for.txt', 'data_files/for.yml', lstrip=False))
