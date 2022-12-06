#!/usr/bin/env python
import os
import sys
import hashlib
from tabulate import tabulate


def writeLog(filename, hashsha1, i):
    try:
        with open('log.txt', 'a') as f:
            f.write(str(filename)+'\t'+str(hashsha1)+'\t'+str(i)+'\n')
    except FileNotFoundError:
        f = open('log.txt', 'w')
        f.close()


def getSHA1(filename):
    sha1sum = hashlib.sha1()
    with open(filename, 'rb') as source:
        block = source.read(2**16)
        while len(block) != 0:
            sha1sum.update(block)
            block = source.read(2**16)
    return(sha1sum.hexdigest())


if __name__ == "__main__":

    tables = []
    headers = ['FileName', 'SHA1', 'Check Dump']
    listFile = os.listdir()
    f = open('log.txt', 'w')
    f.close()
    for i in listFile:
        if(i == 'gethash.py' or i == 'log.txt'):
            continue
        a = i.split('.')
        if(os.path.isfile(os.path.join(os.getcwd(), i))):
            try:

                sha1 = getSHA1(i)
                os.rename(os.path.join(os.getcwd(), i), os.path.join(os.getcwd(), sha1+'.'+str(a[len(a)-1])))
                #writeLog(os.path.join(os.getcwd(), i), sha1, True)
                tables.append(
                    [str(os.path.join(os.getcwd(), i)), str(sha1), "True"])
            except FileExistsError:
                #writeLog(os.path.join(os.getcwd(), i), 'NONE', False)
                tables.append(
                    [str(os.path.join(os.getcwd(), i)), str(sha1), "False"])

    print(tabulate(tables, headers, tablefmt="github"))
    with open('log.txt', 'a') as f:
        f.write(tabulate(tables, headers, tablefmt="github"))
