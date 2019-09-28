'''
-*- coding: utf-8 -*-
@Author  : LiZhichao
@Time    : 2019/8/27 17:17
@Software: PyCharm
@File    : project1.py
'''
import re
import sys

def getAddress(port):
    pattern = r'^\S+'
    f = open('1.txt','r')
    while True:
        data = ''
        for line in f:
            if line != '\n':
                data += line
            else:
                break
        if not data:
            break
        # print(data)
        Port = re.match(pattern,data).group()
        if port == Port:
            # print(data)
            pattern = r'address is (\S+)'
            addr = re.search(pattern,data).group(1)
            print(addr)
            return addr
            # break
        else:
            continue

if __name__ == '__main__':
    # port = sys.argv[1]
    port = input("端口输入：")
    getAddress(port)