# -*- coding: utf-8 -*-
'''
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости от выбранного режима,
задавались разные вопросы в запросе о номере VLANа или списка VLANов:
* для access: 'Enter VLAN number:'
* для trunk: 'Enter allowed VLANs:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
'''

access_template = [
    'switchport mode access', 'switchport access vlan {}',
    'switchport nonegotiate', 'spanning-tree portfast',
    'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan {}'
]

templates = {
  'access': [access_template, 'Enter VLAN number: '],
  'trunk': [trunk_template, 'Enter allowed VLANs: ']
}

mode = input('Enter interface mode (access/trunk): ')
intf = input('Enter interface type and number: ')
vlan = input(templates[mode][1])

print()
print('interface {}'.format(intf))
print('\n'.join(templates[mode][0]).format(vlan))