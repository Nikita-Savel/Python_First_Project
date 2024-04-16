import tkinter as tk
import time
import threading
import random
import pickle
from os.path import exists
from Info import Info

class TypeSpeed:

    def __init__(self):
        # Параметры игрового окна
        self.root = tk.Tk()
        self.root.title("Keyboard trainer")
    
    def set_window_size(self):
        # Размеры окна
        self.weight = 1280
        self.height = 720
        self.root.geometry(f'{self.weight}x{self.height}')
        self.root.resizable(False, False)

    def set_window_color(self):
        # Цвет окна
        self.GRAYISH_YELLOW_PINK = '#CF9284'
        self.root.config(bg = self.GRAYISH_YELLOW_PINK)

    def set_files(self):
        # Открытие файла с ошибками
        if not exists("error_log.pkl"):
           pickle.dump(0, open("error_log.pkl", "wb"))
        self.error_count = pickle.load(open("error_log.pkl", "rb"))

        if not exists("stat.pkl"):
            pickle.dump(0, open("stat.pkl", "wb"))
        self.statistic = pickle.load(open("stat.pkl", "rb"))

        # Загрузка строк из файла
        self.texts = open("extensions/texts.txt", "r").read().split("\n")

        # Функция проверки корректного символа
        self.check = (self.root.register(self.is_valid), "%P")

    def set_window(self):
        # Создание окна для ввода строки
        self.GREY = '#FFFFF0'
        self.frame_one = tk.Frame(self.root, bg = self.GREY)
        self.frame_one.place(relwidth = 0.5, relheight = 0.5)
        self.sentence = random.choice(self.texts)

        # Поле для печати
        self.WHITE = "#FFFFFF"
        self.input_entry = tk.Entry(self.frame_one, width = 78, validate = "key", validatecomman = self.check,
                                    font = ("Times New Roman", 24), background = self.WHITE)
        self.input_entry.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 10)
        self.input_entry.place(relx = 0.01, rely = 0.15, relwidth = 0.98, relheight = 0.08)
        self.input_entry.bind("<KeyRelease>", self.start)

    def set_texts(self):
        # Приветствие
        self.welcome_label = tk.Label(self.root, justify = "center", text = "Keyboard trainer", font = ("Times New Roman", 32),
                                      bg = self.GRAYISH_YELLOW_PINK)
        self.welcome_label.place(relx = 0.25, rely = 0, relwidth = 0.5, relheight = 0.1)
    
        # Текст для ввода
        self.sample_label = tk.Label(self.frame_one, text = self.sentence, font = ("Times New Roman", 24))
        self.sample_label.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 10)
        self.sample_label.place(relx = 0.01, rely = 0.05, relwidth = 0.98, relheight = 0.08)

    def set_view(self):
        # Отображение времени печати
        self.time_label = tk.Label(self.frame_one, text = "Time: 0.0 sec", font = ("Times New Roman", 20))
        self.time_label.grid(row = 3, column = 0, columnspan = 1, padx = 5, pady = 10)
        self.time_label.place(x = 250, y = 300)

        # Отображение скорости печати
        self.speed_label = tk.Label(self.frame_one, text = "Speed: \n 0 CPM \n 0 WPM",
                                    font = ("Times New Roman", 20))
        self.speed_label.grid(row = 2, column = 0, columnspan = 1, padx = 5, pady = 10)
        self.speed_label.place(x = 600, y = 300)

        # Отображение статистики предыдущей попытки
        self.last_attempt_label = tk.Label(self.frame_one,
                                   text = f"Last attempt: \n {self.error_count} errors \n {self.statistic:.0f} CPM",
                                   font = ("Times New Roman", 20))
        self.last_attempt_label.grid(row = 2, column = 0, columnspan = 2, padx = 5, pady = 5)
        self.last_attempt_label.place(x = 900, y = 300)

        # Отображение количества ошибок
        self.error_label = tk.Label(self.frame_one, text = f"0 errors", font = ("Times New Roman", 20))
        self.error_label.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 5)
        self.error_label.place(x = 280, y = 350)

    def set_buttons(self):
        # Кнопка 'Reset'
        self.reset_button = tk.Button(self.frame_one, text = "Reset", command = self.reset, font = ("Times New Roman", 24))
        self.reset_button.grid(row = 4, column = 0, columnspan = 2, padx = 5, pady = 5)
        self.reset_button.place(relx = 0.02, rely = 0.88, relwidth = 0.08, relheight = 0.08)

        # Кнопка открытия 'Help'
        self.help_button = tk.Button(self.frame_one, text = "Help", command = self.open_info, font = ("Times New Roman", 24))
        self.help_button.grid(row = 4, column = 0, columnspan = 2, padx = 5, pady = 5)
        self.help_button.place(relx = 0.9, rely = 0.88, relwidth = 0.08, relheight = 0.08)

        self.frame_one.place(rely = 0.1, relwidth = 1, relheight = 0.9)

    def set_values(self):
        self.error_count = 0
        self.running = False
        self.index = 0
        self.const_time = 0
        self.temporary_time = 0
        self.number_symbols = 0
        self.number_words = 0
        self.detector = True
        self.begin = True
        self.det2 = True
        self.det3 = True

        self.root.mainloop()

    # Начало отсчёта времени
    def start(self, event):
        SHIFT_KEY = 16
        CONTROL_KEY = 17
        ALT_KEY = 18
        if not self.running:
            if not event.keycode in [SHIFT_KEY, CONTROL_KEY, ALT_KEY]:
                self.running = True
                t = threading.Thread(target = self.time_thread)
                t.start()

    # Отображение 'CPM' и 'WPM'
    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.const_time += 0.1
            if self.det2:
                self.temporary_time += 0.1
            if self.det3 != 0:
                tim = self.const_time - self.temporary_time
                if (tim != 0):
                    CPM = self.number_symbols / tim * 60
                    WPM = self.number_words / tim * 60
                else:
                    CPM = 0
                    WPM = 0
                self.time_label.config(text = f"Time: {tim:.1f} sec")
                self.speed_label.config(text = f"Speed: \n {CPM:.0f} CPM \n {WPM:.0f} WPM")
            else:
                self.speed_label.config(text = f"Speed: \n {0:.0f} CPM \n {0:.0f} WPM")

    # Сброс
    def reset(self):
        self.detector = True
        self.error_count = 0
        self.running = False
        self.det2 = True
        self.det3 = True
        self.const_time = 0
        self.temporary_time = 0
        self.number_words = 0
        self.number_symbols = 0
        self.index = 0
        self.sentence = random.choice(self.texts)
        self.speed_label.config(text = "Speed: \n 0 CPM \n 0 WPM")
        self.time_label.config(text = "Time: 0.0 sec")
        ans = pickle.load(open("error_log.pkl", "rb"))
        stat = pickle.load(open("stat.pkl", "rb"))
        self.last_attempt_label.config(text = f"Last attempt: \n {ans} errors \n {stat:.0f} CPM")
        self.error_label.config(text = f"0 errors")
        self.sample_label = tk.Label(self.frame_one, text = self.sentence, font = ("Times New Roman", 24))
        self.sample_label.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 10)
        self.sample_label.place(relx = 0.01, rely = 0.05, relwidth = 0.98, relheight = 0.08)
        self.input_entry.destroy()
        self.input_entry = tk.Entry(self.frame_one, width = 78, validate = "key", validatecomman = self.check,
                                    font = ("Times New Roman", 24), background = self.WHITE)
        self.input_entry.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 10)
        self.input_entry.place(relx = 0.01, rely = 0.15, relwidth = 0.98, relheight = 0.08)
        self.error_label.config(text = f"0 errors")
        self.input_entry.bind("<KeyRelease>", self.start)

    def open_info(self):
        Info()

    # Функция проверки корректности символа
    def is_valid(self, value):
        if self.begin:
            self.begin = False
            self.welcome_label = tk.Label(self.root, justify = 'center', text = "Keyboard trainer", font = ("Times New Roman", 32),
                                      bg = self.GRAYISH_YELLOW_PINK)
            self.welcome_label.place(relx = 0.25, rely = 0, relwidth = 0.5, relheight = 0.1)
        if (self.det2 and len(value) == self.index + 1):
            self.det2 = False
        if (len(value) == len(self.sentence) and value[-1] == self.sentence[self.index]):
            self.index = 0
            self.det2 = True
            self.detector = True
            self.sentence = random.choice(self.texts)
            self.speed_label.config(text="Speed: \n 0 CPM \n 0 WPM")
            CPM = self.number_symbols / (self.const_time - self.temporary_time) * 60
            pickle.dump(CPM, open("stat.pkl", "wb"))
            self.sample_label = tk.Label(text = self.sentence)
            self.input_entry.after_idle(lambda: self.input_entry.configure(validate = "all"))
            self.input_entry.delete(0, tk.END)
            return True

        if (len(value) != 0 and value[-1] == self.sentence[self.index] and len(value) == self.index + 1):
            if value[-1] == " ":
                self.number_words += 1
            self.number_symbols += 1
            self.detector = True
            self.index += 1
            GREY_MOSS = "#787B60"
            self.input_entry.config(fg = GREY_MOSS)
            return True
        else:
            if self.detector:
                self.error_count += 1
                self.detector = False
            self.error_label.config(text = f"{self.error_count} errors")
            pickle.dump(self.error_count, open("error_log.pkl", "wb"))
            BLACK = "#F0241E"
            self.input_entry.config(fg = BLACK)
            return False
