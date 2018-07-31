# -*- coding: utf-8 -*-
'''
Задание 21.1

Переделать скрипт cfg_gen.py в функцию generate_cfg_from_template.

Функция ожидает два аргумента:
* путь к шаблону
* файл с переменными в формате YAML

Функция должна возвращать конфигурацию, которая была сгенерирована.

Проверить работу функции на шаблоне templates/for.txt и данных data_files/for.yml.

'''

from jinja2 import Environment, FileSystemLoader
import yaml
import sys
import os


def generate_cfg_from_template(path_template, path_vars_yaml):
    TEMPLATE_DIR, template_file = os.path.split(path_template)
    vars_dict = yaml.load(open(path_vars_yaml))

    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        trim_blocks=True,
        lstrip_blocks=True)
    template = env.get_template(template_file)
    
    return template.render(vars_dict)