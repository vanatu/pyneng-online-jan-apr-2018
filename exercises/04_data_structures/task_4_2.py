# -*- coding: utf-8 -*-
'''
Задание 4.2

Преобразовать строку MAC из формата XXXX:XXXX:XXXX в формат XXXX.XXXX.XXXX

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

MAC = 'AAAA:BBBB:CCCC'
print('{0[0]}.{0[1]}.{0[2]}'.format(MAC.split(':')))
