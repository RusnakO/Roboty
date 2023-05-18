import math
from tkinter import *

# Функція для обчислення сторони гіпотенузи за катетами
def calculate_hypotenuse():
    # Отримати значення катетів з текстових полів
    side_a = float(side_a_entry.get())
    side_b = float(side_b_entry.get())

    # Обчислити значення гіпотенузи за формулою теореми Піфагора
    hypotenuse = math.sqrt(side_a**2 + side_b**2)

    # Вивести результат у вікні повідомлення
    result_label.config(text=f"Гіпотенуза = {hypotenuse:.2f}")

# Функція для обчислення одного з катетів за гіпотенузою та іншим катетом
def calculate_side():
    # Отримати значення гіпотенузи та одного з катетів
    hypotenuse = float(hypotenuse_entry.get())
    side_c = float(side_c_entry.get())

    # Обчислити значення другого катета за формулою теореми Піфагора
    side_d = math.sqrt(hypotenuse**2 - side_c**2)

    # Вивести результат у вікні повідомлення
    result_label.config(text=f"Катет = {side_d:.2f}")

# Створити головне вікно програми
root = Tk()
root.title("Калькулятор теореми Піфагора")

# Створити елементи вікна: мітки, текстові поля та кнопки
side_a_label = Label(root, text="Катет A")
side_a_entry = Entry(root)
side_b_label = Label(root, text="Катет B")
side_b_entry = Entry(root)
calculate_hypotenuse_button = Button(root, text="Обчислити гіпотенузу", command=calculate_hypotenuse)
hypotenuse_label = Label(root, text="Гіпотенуза")
hypotenuse_entry = Entry(root)
side_c_label = Label(root, text="Катет C")
side_c_entry = Entry(root)
calculate_side_button = Button(root, text="Обчислити катет", command=calculate_side)
result_label = Label(root, text="Результат буде тут", font=("Arial", 16, "bold"))

# Розмістити елементи у вікні за допомогою менеджера геометрії Grid
side_a_label.grid(row=0, column=0, padx=5, pady=5)
side_a_entry.grid(row=0, column=1, padx=5, pady=5)
side_b_label.grid(row=1, column=0, padx=5, pady=5)
side_b_entry.grid(row=1, column=1, padx=5, pady=5)
calculate_hypotenuse_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
hypotenuse_label.grid(row=3, column=0, padx=5, pady=5)
hypotenuse_entry.grid(row=3, column=1, padx=5, pady=5)
side_c_label.grid(row=4, column=0, padx=5, pady=5)
side_c_entry.grid(row=4, column=1, padx=5, pady=5)
calculate_side_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
result_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

# Запустити головний цикл програми
root.mainloop()
