# -*- coding: utf-8 -*-
'''
Задание 21.1b

Дополнить функцию generate_cfg_from_template из задания 21.1 или 21.1a:
* добавить поддержку разных форматов для файла с данными

Должны поддерживаться такие форматы:
* YAML
* JSON
* словарь Python

Сделать для каждого формата свой параметр функции.
Например:
* YAML - yaml_file
* JSON - json_file
* словарь Python - py_dict

Проверить работу функции на шаблоне templates/for.txt и данных:
* data_files/for.yml
* data_files/for.json
* словаре data_dict

'''

data_dict = {
    'vlans': {
        10: 'Marketing',
        20: 'Voice',
        30: 'Management'
    },
    'ospf': [{
        'network': '10.0.1.0 0.0.0.255',
        'area': 0
    }, {
        'network': '10.0.2.0 0.0.0.255',
        'area': 2
    }, {
        'network': '10.1.1.0 0.0.0.255',
        'area': 0
    }],
    'id': 3,
    'name': 'R3'
}

from jinja2 import Environment, FileSystemLoader
import sys, os, yaml, json

def generate_cfg_from_template(path_template, yaml_file=None, json_file=None,
                                py_dict=None, trim=True, lstrip=True):
    TEMPLATE_DIR, template_file = os.path.split(path_template)
    if yaml_file:
        vars_dict = yaml.load(open(yaml_file))
    elif json_file:
        vars_dict = json.load(open(json_file))
    elif py_dict:
        vars_dict = py_dict
    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        trim_blocks=trim,
        lstrip_blocks=lstrip)
    template = env.get_template(template_file)

    return template.render(vars_dict)