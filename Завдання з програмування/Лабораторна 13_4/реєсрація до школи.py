from tkinter import *

def f():
    lab2.config(text="Учень буде навчатися у %d класі" % val.get())
    lab3.config(text="ПІБ учня - %s" % edit1.get())

window = Tk()

lab1 = Label(window, text="Введіть ПІБ учня та виберіть клас")
lab1.pack()

edit1 = Entry(window)
edit1.pack()

val = IntVar()
val.set(1)

for i in range(11):
    Radiobutton(window, text="%d клас" % (i+1), variable=val, value=i+1, command=f).pack()

lab2 = Label(window, fg="red")
lab2.pack()

lab3 = Label(window, fg="red")
lab3.pack()

f()

window.mainloop()
