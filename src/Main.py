from TypeSpeed import TypeSpeed

class Main:

    def __init__(self):
        # Cоздание объекта класса
        my_window = TypeSpeed()
        my_window.set_window_size()
        my_window.set_window_color()
        my_window.set_files()
        my_window.set_window()
        my_window.set_texts()
        my_window.set_view()
        my_window.set_buttons()
        my_window.set_values()

if __name__ == "__main__":
    main_instance = Main()
