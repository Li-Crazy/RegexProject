'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/8/27 15:35
@Software: PyCharm
@File    : project.py
'''
import re

f = open('1.txt')
for line in f:
    pattern = r"^[a-zA-Z][_./0-9a-zA-Z]*"
    l = re.findall(pattern,line)
    if l:
        print("++++++++")
        print(l)
    ip = re.findall('address is ([./0-9a-zA-Z]*)',line)
    if ip:
        print(ip)



