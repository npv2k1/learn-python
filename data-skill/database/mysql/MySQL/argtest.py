import os
from sys import argv
argv.remove('argtest.py')
ls = ' '.join(argv)
as1 = ls.split('.')
eng = as1[0]
vni = as1[1]

print(eng)
print(vni)
# def toFile(eng, vni):
#     try:
#         with open('a.txt', 'a', encoding='utf-8') as f:
#             string = eng + ' : ' + vni
#             string = string.ljust(50, ' ')
#             f.write(string+'\n')
#             #print(string)
#             pass
#     except FileNotFoundError:
#         f = open("a.bin", "w")
#         f.close()
#         pass


# def outFile(eng):
#     try:
#         with open('a.txt', 'r', encoding='utf-8') as f:
#             a = f.readlines(1)
#             while(len(a) != 0):
#                 if(a[0].strip().split(' : ')[0] == eng):
#                     return a[0].strip().split(' : ')[1]
#                 a = f.readlines(1)
#             pass
#     except FileNotFoundError:
#         f = open("a.bin", "w")
#         f.close()
#         pass


# if(vni == '0'):
#     print(outFile(eng))
# else:
#     toFile(eng, vni)
