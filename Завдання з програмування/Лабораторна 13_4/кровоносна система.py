from tkinter import *

def confirm():

   message_label.config(text="Молодець! У тебе добрі знання з біології!")

def deny():

   message_label.config(text="Ти помилився!!!")



window = Tk()

window.title("Кровоносна система")



label = Label(window, text="Кров виносить із клітин продукти розпаду, що утворюються в результаті їх життєдіяльності")

label.pack(padx=10, pady=10)


confirm_button = Button(window, text="Погоджуюсь", bg="green", fg="white", command=confirm)

confirm_button.pack(padx=10, pady=5)

deny_button = Button(window, text="Не погоджуюсь", bg="red", fg="white", command=deny)

deny_button.pack(padx=10, pady=5)



message_label = Label(window, text="")

message_label.pack(padx=10, pady=10)



window.mainloop()
