import tkinter as tk
from tkinter import ttk
from mainframe import MainFrame


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Currency Converter")

        mainframe = MainFrame(self)
        mainframe.grid()


if __name__ == "__main__":
    app = App()

    app.mainloop()