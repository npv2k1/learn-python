#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import cv2
import time
import os
speed = 0.05 # float(input('Speed: '))
# Đọc file
a = list(open('pic.txt', 'r', encoding='UTF-8').read().split('\n'))

# hàm xóa màn hình console


def clear(): return os.system('clear')


def move(y, x):
    print("\033[%d;%dH" % (y, x))
i=0
# while(True):
#     print('0'*i)
#     i+=1
#     time.sleep(1)
#     move(0,0)





x = max(map(lambda i: len(i), a))
k = 0
while k < x:
    # in cac dong trong a
    for i in a:
        if(len(i) == 0):
            continue
        if(k > len(i)):
            print('\x1b[0;33;40m' + i[:len(i)] + '\x1b[0m')
        else:
            print('\x1b[0;33;40m' + i[:k+1] + '\x1b[1m')
        

    time.sleep(speed)
    k += 1
    if(k != x):
        move(0, 0)
    
# img = cv2.imread('img.png')
# cv2.imshow("Happy birthday",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
