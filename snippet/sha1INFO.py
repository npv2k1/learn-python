#!/usr/bin/env python
'''
Đây là code giúp kiểm tra sha1 của từng file và lưu dưới dạng một file test INFO_tên file.txt
'''

import os
import sys
import hashlib


def getSHA1(filename):
    sha1sum = hashlib.sha1()
    with open(filename, 'rb') as source:
        block = source.read(2**16)
        while len(block) != 0:
            sha1sum.update(block)
            block = source.read(2**16)
    return(sha1sum.hexdigest())


listFile = os.listdir()
for i in listFile:
    if i == 'sha1INFO.py':
        continue
    a = i.split('.')
    file = i.split('.'+str(a[len(a)-1]))
    print(str(i)+'\t'+'done!')
    if(os.path.isfile(os.path.join(os.getcwd(), i))):
        shaFile = getSHA1(i)
        with open(f'INFO_{file[0]}.txt', 'w', encoding='utf-8')as f:
            f.write(str(i)+'\n'+'SHA1: '+shaFile)
            print(f'\tINFO_{file[0]}.txt')
        # try:
        #     os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(),getSHA1(i)+'.'+str(a[len(a)-1])))
        # except FileExistsError:
        #     print(os.path.join(os.getcwd(), i))
