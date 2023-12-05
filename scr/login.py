import tkinter as tk
from tkinter import messagebox
import sqlite3


class Logger:
    
    last_logged_in_user = None # global variable to store last logged in user
    login = None # instance variable to store login

    def __init__(self, master):
        self.master = master
        self.init_ui()

    def init_ui(self):
        self.login_label = tk.Label(self.master, text="Login:", font=("Arial", 16))
        self.login_entry = tk.Entry(self.master, font=("Arial", 16))

        self.password_label = tk.Label(self.master, text="Senha:", font=("Arial", 16))
        self.password_entry = tk.Entry(self.master, font=("Arial", 16), show="*")

        self.login_button = tk.Button(self.master, text="Entrar", command=self.login, font=("Arial", 16))

        self.login_label.grid(row=0, column=0, padx=10, pady=10)
        self.login_entry.grid(row=0, column=1, padx=10, pady=10)

        self.password_label.grid(row=1, column=0, padx=10, pady=10)
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        self.login_button.grid(row=2, column=1, padx=10, pady=10)

    def login(self):
        login = self.login_entry.get()
        password = self.password_entry.get()

        conn = sqlite3.connect('user_data.db')
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM users WHERE login = ? AND password = ?", (login, password))
            result = cursor.fetchone()

            if result:
                messagebox.showinfo("Sucesso", "Logado com sucesso! Bem vindo")
                self.master.destroy()
                 # set global variable
                from index import run
                run()
            else:
                messagebox.showerror("Erro", "Login ou senha incorretos!")
        except sqlite3.Error as e:
            messagebox.showerror("Erro", f"Erro ao executar consulta: {e}")


if __name__ == "__main__":
    app = tk.Tk()
    app.title("Adega Olaria System")
    Logger(app)
    app.geometry("300x200")
    app.mainloop()