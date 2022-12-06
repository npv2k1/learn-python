from sys import getsizeof
import pickle
class sv():
    def __init__(self):
        super().__init__()
        self.name=""
        self.age=""
    def calMe(self):
        print('{} {} tuoi'.format(self.name, self.age))
a=sv()
asv=[]
asv.append(a)
f = open("sv.bin", "rb")
a=pickle.load(f)
a.calMe()
a = pickle.load(f)
a.calMe()
a = pickle.load(f)
a.calMe()
