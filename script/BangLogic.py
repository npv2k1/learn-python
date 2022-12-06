'''
Bảng logic NOR
'''
def nor(a=0,b=0):
    return 1 if (not (a or b)) else 0
def out(x):
    for i in (0,1):
        for j in (0,1):
            print(str(i)+"\t"+str(j)+"\t"+str(nor(i,j)))
if __name__ == "__main__":
    out(nor)
