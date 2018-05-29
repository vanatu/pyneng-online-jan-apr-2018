# -*- coding: utf-8 -*-
'''
Задание 5.1b

Преобразовать скрипт из задания 5.1a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''
from sys import argv
ip = argv[1]
mask = int(argv[2])

list_dec_IP = [int(i) for i in ip.split('.')]
list_bin_IP = ['{0:08b}'.format(i) for i in list_dec_IP]

seq_bin_net = ''.join(list_bin_IP)[:mask] + '0' * (32 - mask)
list_bin_net = [seq_bin_net[i:i+8] for i in range(0,32,8)]
list_dec_net = [int(i,2) for i in list_bin_net]

seq_bin_mask = '1' * mask + '0' * (32 - mask)
list_bin_mask = [seq_bin_mask[i:i+8] for i in range(0,32,8)]
list_dec_mask = [int(i,2) for i in list_bin_mask]

print('''Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}

Mask:
/{4}'''.format(*list_dec_net, mask))
print('{0:<10}{1:<10}{2:<10}{3:<10}'.format(*list_dec_mask))
print('{0:08b}  {1:08b}  {2:08b}  {3:08b}'.format(*list_dec_mask))
