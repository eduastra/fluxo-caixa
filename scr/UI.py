import tkinter as tk
from tkinter import ttk
from datetime import datetime
from login import Logger


class Application:
    def __init__(self, master):
        self.master = master
        self.init_ui()

    def init_ui(self):
        self.buttons = [
            tk.Button(self.master, text="Venda", command=lambda: print(Logger.last_logged_in_user), font=("Arial", 22)),
            tk.Button(self.master, text="Entrada", command=lambda: print("Botão Entrada clicado"), font=("Arial", 22)),
            tk.Button(self.master, text="Estoque", command=lambda: print("Botão Estoque clicado"), font=("Arial", 22)),
            tk.Button(self.master, text="Relatório", command=lambda: print("Botão Relatório clicado"), font=("Arial", 22)),
            tk.Button(self.master, text="Logout", command=lambda: print("Botão Logout clicado"), font=("Arial", 22))
        ]

        self.clock_label = ttk.Label(self.master, text="", font=("Arial", 70))

        self.display_home()

        self.master.bind("<F11>", self.toggle_full_screen)
        
        # Adicione esta linha para iniciar o relógio
        self.update_clock()

    def display_home(self):
        for i in range(len(self.buttons)):
            self.buttons[i].grid(row=i, column=4, pady=20, padx=600)

        self.clock_label.grid(row=6, column=4, pady=50)

        self.center_buttons()

    def center_buttons(self):
        window_width = self.master.winfo_width()
        window_height = self.master.winfo_height()
        frame = ttk.Frame(self.master)

        frame_width = frame.winfo_width()
        frame_height = frame.winfo_height()

        horizontal_position = (window_width - frame_width) / 2
        vertical_position = (window_height - frame_height) / 2

        frame.place(x=horizontal_position, y=vertical_position)

    def toggle_full_screen(self, event):
        self.master.attributes("-fullscreen", not self.master.attributes("-fullscreen"))

    def update_clock(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.clock_label.config(text=current_time)
        self.clock_label.after(1000, self.update_clock)

    def on_resize(self, event):
        self.center_buttons()
        self.update_clock()