import random
#listchar ='1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'
listchar ='1234567890QWERTYUIOPASDFGHJKLZXCVBNM'

key=[]
f=open('key.txt','w')
dem=1
while True:
    key=[]
    for i in range(1,6):
        key.append(''.join(random.choices(listchar,k=5)))
        
        
    f.write('-'.join(key)+'\n')   
    if(dem==10000):
        break
    dem+=1
f.close()
