from tkinter import *
import random
root = Tk()


def clamp(x):
  return max(0, min(x, 255))


def changeButtonColor():
    colors = "#{0:02x}{1:02x}{2:02x}".format(
        clamp(random.randint(0, 225)), clamp(random.randint(0, 225)), clamp(random.randint(0, 225)))
    btn1['bg'] = colors
    btn1['text'] = "Random Color" +'\n' + colors



btn1 = Button(root, text="Random Color", padx=100, pady=100, command=changeButtonColor)
e=Entry(btn1,bg='black',width=50)
btn1.pack()
root.mainloop()
