#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
f = open('pic.txt', 'r', encoding='UTF-8')
string1 = f.read()
a = list(string1.split('\n'))


def clear(): return os.system('cls')


clear()
k = 0
while k < len(a[1]):
    for i in a:
        if (len(i) == 0):
            break

        print('\x1b[7;30;43m' + i[:k+1] + '\x1b[0m')

    time.sleep(0.05)
    k += 1
    if (k != len(a[1])):
        clear()
