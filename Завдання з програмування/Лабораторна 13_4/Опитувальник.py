import tkinter as tk
from tkinter import messagebox

class MathQuiz:
    def __init__(self, master):
        self.master = master
        self.master.title("Опитувальник з математики")

        # Питання та відповіді
        self.questions = {
            "1. 2 + 2 = 4? ": "так",
            "2. 5 * 5 = 25? ": "так",
            "3. 10 - 3 = 6? ": "ні",
            "4. 7 / 2 = 3,5? ": "так",
            "5. 3^2 = 9? ": "так"
        }

        # Інтерфейс для питань та відповідей
        self.question_label = tk.Label(self.master, text="")
        self.question_label.pack()

        self.yes_button = tk.Button(self.master, text="Так", command=self.check_answer_yes)
        self.yes_button.pack(side=tk.LEFT)

        self.no_button = tk.Button(self.master, text="Ні", command=self.check_answer_no)
        self.no_button.pack(side=tk.RIGHT)

        self.answer_label = tk.Label(self.master, text="")
        self.answer_label.pack()

        # Початкове питання
        self.question_number = 0
        self.ask_question()

    def ask_question(self):
        question = list(self.questions.keys())[self.question_number]
        self.question_label.config(text=question)

    def check_answer_yes(self):
        answer = list(self.questions.values())[self.question_number]
        self.show_answer(answer, "так")

    def check_answer_no(self):
        answer = list(self.questions.values())[self.question_number]
        self.show_answer(answer, "ні")

    def show_answer(self, correct_answer, user_answer):
        if correct_answer == user_answer:
            self.answer_label.config(text="Відповідь вірна!")
        else:
            messagebox.showerror("Помилка", "Відповідь неправильна.")
        if self.question_number < len(self.questions) - 1:
            self.question_number += 1
            self.ask_question()
        else:
            self.question_label.config(text="Опитування завершено!")
            self.yes_button.config(state=tk.DISABLED)
            self.no_button.config(state=tk.DISABLED)

root = tk.Tk()
app = MathQuiz(root)
root.mainloop()
