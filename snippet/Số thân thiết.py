import math
x=int(input())
a=[]
for i in range(1,int(x**(1/2))+1):
    if(x%i==0):
        if(i==x**(1/2)):
            a.append(i)
            break
        a.append(i)
        a.append(int(x/i))
a.sort()
print(a)

