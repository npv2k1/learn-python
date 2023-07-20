from tkinter import *

root = Tk()

check = False


def click(e,num):
    global check
    if e:
        dictButton[num]['text']="X"
        check=not check
    else:
        dictButton[num]['text'] = "O"
        check=not check
   
btn1 = Button(root, text="", padx=50, pady=50 ,command=lambda: click(check, 1))
btn2 = Button(root, text="", padx=50, pady=50, command=lambda: click(check,2))
btn3 = Button(root, text="", padx=50, pady=50, command=lambda: click(check, 3))
btn4 = Button(root, text="", padx=50, pady=50, command=lambda: click(check,4))
btn5 = Button(root, text="", padx=50, pady=50, command=lambda: click(check,5))
btn6 = Button(root, text="", padx=50, pady=50, command=lambda: click(check,6))
btn7 = Button(root, text="", padx=50, pady=50, command=lambda: click(check,7))
btn8 = Button(root, text="", padx=50, pady=50, command=lambda: click(check,8))
btn9 = Button(root, text="", padx=50, pady=50, command=lambda: click(check,9))

dictButton = {
    1: btn1,
    2: btn2,
    3: btn3,
    4: btn4,
    5: btn5,
    6: btn6,
    7: btn7,
    8: btn8,
    9: btn9,
}

btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)


root.mainloop()
