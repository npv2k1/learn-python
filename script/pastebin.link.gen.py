import requests
import random
import os
import time
#tạo một mảng chứa các kí tự
charlis='1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
#lấy ngẫu nhiên trong mảng 8 ký tự
while True:
    path=random.choices(charlis,k=8)
    link='https://pastebin.com/'+''.join(path)
    res=requests.get(link)
    time.sleep(1)
    try:
        f = open("pastebin.txt")
        # Do something with the file
    except IOError:
        f = open("pastebin.txt",'w')
    finally:
        f.close()
    f=open("pastebin.txt",'a')
    if(res.status_code==200):
        f.write(link+"\n")
    else:
        print("continue")
