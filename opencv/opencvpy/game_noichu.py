def check(str1,str2):
    if(str1[len(str1)-1]==str2[0]):
        return True
    else:
        return False
if __name__ == "__main__":
    pass
    while True:
        a=input('Bạn 1: ')
        b=input('Bạn 2: ')
        while not( check(a,b) or check(b,a)):
            if(not check(a,b)):
                a=input('Bạn 1 nhập lại: ')
            if(not check(b,a)):
                b=input('Bạn 1 nhập lại: ')
