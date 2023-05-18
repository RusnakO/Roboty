from tkinter import*
def btn_click():
    if cvar1.get()==1:root.title('Заголовок змінений')
    if cvar2.get()!=0:root['bg']='red'
    if cvar3.get()!=0:root.geometry('500x200')
root=Tk()
cvar1 = IntVar()
c1 = Checkbutton(text="Заголовок",font='Arial 12 ', variable = cvar1, onvalue=1, offvalue=0)
c1.place(x = 10, y = 10)
cvar2 = IntVar()
c2 = Checkbutton(text="Колір",font='Arial 12 ', variable = cvar2, onvalue=1, offvalue=0)
c2.place(x = 10, y = 40)
cvar3 = IntVar()
c3 = Checkbutton(text="Розміри",font='Arial 12 ', variable = cvar3, onvalue=1, offvalue=0)
c3.place(x = 10, y = 70)
btn = Button(root, text='Змінити', font='Arial 12', command = btn_click)
btn.place( x= 50, y = 100)
root.mainloop()
