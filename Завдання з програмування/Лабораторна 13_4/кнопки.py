import tkinter

window = tkinter.Tk()
window.title('Різнокольорові кнопки')
window.geometry("220x100")

button1 = tkinter.Button(window, text='Червоний', bg='red', fg='white', width=5, height=1)
button1.pack(side=tkinter.LEFT, padx=5, pady=5)

button2 = tkinter.Button(window, text='Синій', bg='blue', fg='white', width=10, height=2)
button2.pack(side=tkinter.TOP, padx=5, pady=5)

button3 = tkinter.Button(window, text='Зелений', bg='green', fg='white', width=15, height=3)
button3.pack(side=tkinter.BOTTOM, padx=5, pady=5)

button4 = tkinter.Button(window, text='Жовтий', bg='yellow', fg='black', width=20, height=4)
button4.pack(side=tkinter.RIGHT, padx=5, pady=5)

window.mainloop()
