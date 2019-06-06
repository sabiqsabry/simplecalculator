from tkinter import *
from tkinter import ttk

#the addition function
def addition(event):
    x = int(fentry.get())
    y = int(eentry.get())

    sum = x + y

    outputentry.delete(0, "end")
    outputentry.insert(0, sum)
    return

#the subtraction function
def subtraction(event):
    p = int(fentry.get())
    q = int(eentry.get())

    subb = p - q

    outputentry.delete(0, "end")
    outputentry.insert(0, subb)
    return

#the multiplication function
def multiplication(event):
    w = int(fentry.get())
    e = int(eentry.get())

    mull = w * e

    outputentry.delete(0, "end")
    outputentry.insert(0, mull)
    return

#the division function
def division(event):
    t = int(fentry.get())
    y = int(eentry.get())

    divv = t / y

    outputentry.delete(0, "end")
    outputentry.insert(0, divv)
    return

root = Tk()

#the layout
Label(root, text = "Calculator").grid(row=0, columnspan=3)

Label(root, text = "First Number: ").grid(row=1, sticky = W)
Label(root, text = "Second Number: ").grid(row=2, sticky = W)

fentry = Entry(root)
fentry.grid(row=1, column = 1)
eentry = Entry(root)
eentry.grid(row=2, column = 1)

#the choosing of what calculation is needed by the user
Label(root, text= "What do you want to do ?:").grid(row=3, sticky = W)

#the function buttons

plus = Button(root, text = "Add")
plus.bind("<Button-1>", addition)
plus.grid(row=4)
minus = Button(root, text = "Subtract")
minus.bind("<Button-1>", subtraction)
minus.grid(row=5)
multiply = Button(root, text = "Multiply")
multiply.bind("<Button-1>", multiplication)
multiply.grid(row=6)
divide = Button(root, text = "Divide")
divide.bind("<Button-1>", division)
divide.grid(row=7)

Label(root, text= "The answer is: ").grid(row=8)

#the output statement using an entry

outputentry = Entry(root)
outputentry.grid(row=8, column = 1, sticky = W)

root.mainloop()
