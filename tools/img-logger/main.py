from datetime import datetime
from datetime import date
import pyautogui
import os
import datetime
import time

index = int(open('config.ini', 'r+').read().split('=')[1])


def captureScreen(filename):
    # check if img folder exists
    if not os.path.exists('img'):
        os.makedirs('img')

    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(os.path.join(os.getcwd(), 'img', filename))


f = open('log.txt', 'w')
f.close()
while True:
    filename = str(index)+str(datetime.datetime.now())+'.png'
    f = open('log.txt', 'a')
    f.write(str(index)+'\t' + str(datetime.datetime.now())+'.png'+'\n')
    f.close()
    captureScreen(str(index)+'.png')
    index += 1
    time.sleep(10)
    print(index)
