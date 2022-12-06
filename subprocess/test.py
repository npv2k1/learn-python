import time

c = time.time()
sums=0
for i in range(1,10000000):
    sums+=i
print(sums, "=> ", time.time()-c)