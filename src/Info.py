import tkinter as tk

class Info:

    def __init__(self):
        # Параметры окна 'Info'
        self.height = 300
        self.weight = 300
        self.root = tk.Tk()
        self.root.title("Information about playing")
        self.root.geometry(f'{self.height}x{self.weight}')
        self.root.resizable(False, False)
        WHITE = '#FFFFFF'
        self.root.config(bg = WHITE)

        # Создание текста
        self.label = tk.Label(self.root, justify = 'left', text = open("info.txt", "r").read(), font = ("Times New Roman", 18),
                              bg = WHITE)
        self.label.pack()

        # При нажатии на кнопку 'Exit' окно закрывается
        self.button_end = tk.Button(self.root, text = 'Exit',
                                    font = ("Times New Roman", 18), command = self.root.destroy)
        self.button_end.place(relx = 0.5, rely = 0.5, relwidth = 0.05, relheight = 0.05)
        self.button_end.pack()
        self.root.mainloop()
