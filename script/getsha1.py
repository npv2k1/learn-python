#!/usr/bin/env python
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
    a=i.split('.')
    if(os.path.isfile(os.path.join(os.getcwd(),i))):
        try:
            os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(),getSHA1(i)+'.'+str(a[len(a)-1])))
        except FileExistsError:
            print(os.path.join(os.getcwd(), i))
