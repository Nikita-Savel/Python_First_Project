import tkinter as tk

class Info:

    def __init__(self):
        # Параметры окна 'Info'
        self.height = 400
        self.weight = 400
        self.root = tk.Tk()
        self.root.title("Information about playing")
        self.root.geometry(f'{self.height}x{self.weight}')
        self.root.resizable(False, False)
        LAZUR_COLOR = '#96EEDE'
        self.root.config(bg = LAZUR_COLOR)

        # Создание метки с текстом
        GOLD_COLOR = '#FFD700'
        self.label = tk.Label(self.root, text = open("info.txt", "r").read(), font = ("Times New Roman", 12),
                              bg = GOLD_COLOR)
        self.label.pack()

        # При нажатии на кнопку окно закрывается
        self.button_end = tk.Button(self.root, text = 'Clear', font = ("Times New Roman", 16), command = self.root.destroy,
                                    bg = GOLD_COLOR)
        self.button_end.pack()
        self.root.mainloop()
