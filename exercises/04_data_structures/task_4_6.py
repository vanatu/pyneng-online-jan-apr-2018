# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
_, prfx, ad_mtr, _, nh, l_upd, o_intf = ospf_route.replace(',','').split()
print('''{:<23}{}
{:<23}{}
{:<23}{}
{:<23}{}
{:<23}{}
{:<23}{}
'''.format('Protocol:', 'OSPF', 'Prefix:', prfx, 'AD/Metric:', ad_mtr.strip('[]'),
    'Next-Hop:', nh, 'Last update:', l_upd, 'Outbound Interface:', o_intf))
