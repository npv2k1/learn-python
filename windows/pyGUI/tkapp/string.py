import math


def is_isogram(string):
    string = string.lower()
    
    if len(string) <= 1:
        return True
    else:
        for i in range(0, len(string)):
            j = i+1
            dem = 0
            while j < len(string):
                
                if(string[j] == string[i] and dem<=1):  
                                   
                    return False
                dem += 1
                j += 1
       
        return True


print(is_isogram('moOse'))
