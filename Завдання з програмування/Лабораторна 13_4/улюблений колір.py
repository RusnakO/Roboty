from tkinter import *

# створення головного вікна
root = Tk()

# змінна для зберігання вибраного користувачем кольору
val = StringVar()

# задання початкового значення
val.set("blue")

# функція для зміни кольору фону
def change_color():
    color = val.get()
    if color == "blue":
        label.config(bg="blue")
    elif color == "yellow":
        label.config(bg="yellow")
    elif color == "red":
        label.config(bg="red")
    elif color == "green":
        label.config(bg="green")
    
# створення перемикачів
blue_rb = Radiobutton(root, text="Синій", variable=val, value="blue", command=change_color)
yellow_rb = Radiobutton(root, text="Жовтий", variable=val, value="yellow", command=change_color)
red_rb = Radiobutton(root, text="Червоний", variable=val, value="red", command=change_color)
green_rb = Radiobutton(root, text="Зелений", variable=val, value="green", command=change_color)

# розміщення перемикачів на вікні
blue_rb.pack()
yellow_rb.pack()
red_rb.pack()
green_rb.pack()

# створення текстового напису
label = Label(root, text="Текст", bg="white")
label.pack()

# запуск програми на виконання
root.mainloop()
