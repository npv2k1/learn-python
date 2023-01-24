x=int(input())
a=x
i=0
b=0
while(a>0):
    i=int(a%10)
    a=(a-i)/10
    b=b*10+i
print(b)

