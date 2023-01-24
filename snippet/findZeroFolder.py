import os
import sys
import hashlib
from tabulate import tabulate

currentPath=os.getcwd()

listDir= os.listdir()
for i in listDir:
    sublist=os.listdir(os.path.join(currentPath,i))
    