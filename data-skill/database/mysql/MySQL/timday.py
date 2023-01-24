a=[-3,3,-4,4,5,-5]
sum=0
for num in range(1,len(a)+2): #1,2,3,4
    for i in range(1,len(a)+1-num):#4,3,2,1
        sum=0
        for j in range(i,i+num+1):
            sum+=a[j-1]
        print("%d %d %d"%(i,j,sum))