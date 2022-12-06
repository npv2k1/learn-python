def move (y, x):
    print("\033[%d;%dH" % (y, x))
print("hello")
move(0,0)
input()
