import random
dictNum = {
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
}
for i in range(1, 10000):
    a = random.randint(1, 6)
    dictNum[a]+=1
print(dictNum)
