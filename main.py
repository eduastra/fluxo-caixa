import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
import sqlite3


user = None

now = datetime.now()
date_time = now.strftime("%d/%m/%Y %H:%M:%S")

def get_items():
        # Criar conexão com o banco de dados
        conn = sqlite3.connect('warehouse.db')

        # Criar cursor para executar comandos SQL
        cursor = conn.cursor()

        # Executar consulta SQL para obter todos os itens da tabela pricing
        cursor.execute("SELECT item FROM pricing")

        # Obter todos os itens como uma tupla e armazenar na variável items
        items = cursor.fetchall()

        # Fechar a conexão com o banco de dados
        conn.close()

        return items


def connect_db():
    conn = sqlite3.connect('warehouse.db')
    cursor = conn.cursor()
    return conn, cursor

def insert_sale_into_db(item, quantity, payment_method, user):
    conn, cursor = connect_db()
    
    cursor.execute("""
    INSERT INTO sales (item, quantity, payment_method, date, user)
    VALUES (?, ?, ?, ?, ?)
    """, (item, quantity, payment_method, date_time, user))
    
    conn.commit()
    conn.close()


class Application:
    def __init__(self, master):
        self.master = master
        self.init_ui()
        self.update_clock_id = None
        self.get_items = get_items()


    def init_ui(self):
        self.buttons = [
            tk.Button(self.master, text="Venda", command=self.sell_window, font=("Arial", 22)),
            tk.Button(self.master, text="Entrada", command=self.entry_window, font=("Arial", 22)),
            tk.Button(self.master, text="Cadastrar novo item", command=self.register_item, font=("Arial", 22)),
            tk.Button(self.master, text="Relatório", command=lambda: print("Botão Relatório clicado"), font=("Arial", 22)),
            tk.Button(self.master, text="Logout", command=self.logout, font=("Arial", 22))
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

    def sell_window(self):
        # Crie uma nova janela (Toplevel)
        sell_window = tk.Toplevel(self.master)
        sell_window.title("Venda")


        # Adicione os elementos de entrada necessários
        conn = sqlite3.connect('warehouse.db')
        cursor = conn.cursor()

        
        # Adicione os elementos de entrada necessários
        item_label = ttk.Label(sell_window, text="Item:")
        item_combobox = ttk.Combobox(sell_window, state="readonly")
        item_combobox["values"] = get_items()
        item_combobox.grid(row=0, column=1)
        

        payment_method_label = ttk.Label(sell_window, text="Forma de pagamento:")
        payment_method_var = tk.StringVar()
        payment_method_combobox = ttk.Combobox(sell_window, textvariable=payment_method_var, state="readonly")
        payment_method_combobox["values"] = ("Dinheiro", "PIX", "Crédito", "Débito")
        payment_method_combobox.grid(row=2, column=1)

        quantity_label = ttk.Label(sell_window, text="Quantidade:")
        quantity_entry = ttk.Entry(sell_window)

        
        # Adicione um botão para registrar a venda e fechar a janela
        def register_sale():
            item = item_combobox.get()
            quantity = quantity_entry.get()
            payment_method = payment_method_var.get()


            # Registre a venda no sistema (você pode precisar ajustar isso de acordo com a sua lógica atual)
            print(f"Venda registrada: {item}, {quantity}, {payment_method}")

            insert_sale_into_db(item, quantity, payment_method, user)


            conn.commit()
            conn.close()

            # Feche a janela
            sell_window.destroy()


        register_sale_button = tk.Button(sell_window, text="Registrar venda", command=register_sale)

        # Posicione os elementos na janela
        item_label.grid(row=0, column=0)
        item_combobox.grid(row=0, column=1)

        payment_method_label.grid(row=1, column=0)
        payment_method_combobox.grid(row=1, column=1)

        quantity_label.grid(row=2, column=0)
        quantity_entry.grid(row=2, column=1)

        register_sale_button.grid(row=3, column=1)

    def entry_window(self):
        # Crie uma nova janela (Toplevel)
        entry_window = tk.Toplevel(self.master)
        entry_window.title("Entrada")

        # Adicione os elementos de entrada necessários
        item_label = ttk.Label(entry_window, text="Item:")
        item_combobox = ttk.Combobox(entry_window, state="readonly")
        item_combobox["values"] = get_items()
        item_combobox.grid(row=0, column=1)

        quantity_label = ttk.Label(entry_window, text="Quantidade:")
        quantity_entry = ttk.Entry(entry_window)

        # Adicione um botão para registrar a entrada e fechar a janela
        def register_entry():
            item = item_combobox.get()
            quantity = quantity_entry.get()

            # Conecte-se ao banco de dados (ou crie um novo se não existir)
            conn = sqlite3.connect('warehouse.db')

            # Crie uma tabela chamada 'entries' se ela ainda não existir
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS entries
                               (item TEXT, quantity INTEGER, date_time TEXT)''')

            # Registre a entrada no banco de dados
            now = datetime.now()
            date_time = now.strftime("%d/%m/%Y %H:%M:%S")
            cursor.execute("INSERT INTO entries VALUES (?, ?, ?)", (item, quantity, date_time))

            # Salve as alterações e feche a conexão
            conn.commit()
            conn.close()

            # Feche a janela
            entry_window.destroy()

        register_entry_button = tk.Button(entry_window, text="Registrar entrada", command=register_entry)

        # Posicione os elementos na janela
        item_label.grid(row=0, column=0)
        item_combobox.grid(row=0, column=1)

        quantity_label.grid(row=1, column=0)
        quantity_entry.grid(row=1, column=1)

        register_entry_button.grid(row=2, column=1)

    def register_item(self):
        item_window = tk.Toplevel(self.master)
        item_window.title("Cadastrar novo item")
        item_window.geometry("400x200")

        # Adicione os widgets necessários à janela item_window

        create_item_button = tk.Button(item_window, text="Cadastrar novo item", command=self.create_item, font=("Arial", 14))
        update_item_button = tk.Button(item_window, text="Alterar item existente", command=self.update_item, font=("Arial", 14))

        create_item_button.pack()
        update_item_button.pack()

        item_window.mainloop()

    def create_item(self):
        item_window = tk.Toplevel(self.master)
        item_window.title("Cadastrar novo item")
        item_window.geometry("400x200")

        # Create widgets
        tk.Label(item_window, text="Nome do item:").pack()
        item_name = tk.Entry(item_window)
        item_name.pack()

        tk.Label(item_window, text="Preço:").pack()
        item_price = tk.Entry(item_window)
        item_price.pack()

        save_button = tk.Button(item_window, text="Salvar", command=lambda: self.save_item(item_name.get(), item_price.get(), item_window), font=("Arial", 14))
        save_button.pack()

        item_window.mainloop()

    def save_item(self, item_name, item_price, item_window):
    # Verificar se os campos de nome e preço estão preenchidos
        if item_name == "" or item_price == "":
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
            return

        try:
            connection = sqlite3.connect("warehouse.db")
            cursor = connection.cursor()

            # Verificar se o item já existe
            cursor.execute("SELECT * FROM pricing WHERE item = ?", (item_name,))
            existing_item = cursor.fetchone()

            if existing_item:
                messagebox.showerror("Erro", "Item já existe no banco de dados.")
                return

            # Inserir o item no banco de dados
            cursor.execute("INSERT INTO pricing (item, price) VALUES (?, ?)", (item_name, item_price))

            # Salvar as alterações e fechar a conexão
            connection.commit()
            messagebox.showinfo("Sucesso", "Item salvo com sucesso")

        except Exception as e:
            messagebox.showerror("Erro", str(e))

        finally:
            connection.close()
            item_window.destroy()


    def update_item(self):
        update_item_window = tk.Toplevel(self.master)
        update_item_window.title("Alterar item existente")
        update_item_window.geometry("400x200")

        # Adicione os widgets necessários à janela update_item_window
        item_label = ttk.Label(update_item_window, text="Item:", font=("Arial", 14))
        item_combobox = ttk.Combobox(update_item_window, state="readonly")
        item_combobox["values"] = get_items()

        price_label = tk.Label(update_item_window, text="Novo preço:", font=("Arial", 14))
        price_entry = tk.Entry(update_item_window, font=("Arial", 14))

        update_item_button = tk.Button(update_item_window, text="Alterar item", 
                                    command=lambda: self.change_item(item_combobox.get(), price_entry.get()), 
                                    font=("Arial", 14))

        item_label.grid(row=0, column=0) # Posicione a label corretamente
        item_combobox.grid(row=0, column=1) # Posicione o combobox corretamente
        price_label.grid(row=1, column=0)
        price_entry.grid(row=1, column=1)
        update_item_button.grid(row=2, column=0, columnspan=2)
        

    def change_item(self, item, new_price):
        item = str(item).replace("{","").replace("}","")
        print(item)
        # Conexão com o banco de dados SQLite
        connection = sqlite3.connect("warehouse.db")
        cursor = connection.cursor()

        # Executa o comando UPDATE para alterar o preço do item
        cursor.execute("UPDATE pricing SET price = ? WHERE item = ?", (new_price, item))

        # Fecha a conexão com o banco de dados
        connection.commit()
        connection.close()
        messagebox.showinfo("Sucesso", "Logado com sucesso! Bem vindo")
        self.update_item_window.destroy()


    def logout(self):
        global user
        user = None
        self.master.destroy()
        logging()


class Logger:

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
        global user
        login = self.login_entry.get()
        user = login
        password = self.password_entry.get()

        conn = sqlite3.connect('warehouse.db')
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT * FROM users WHERE login = ? AND password = ?", (login, password))
            result = cursor.fetchone()

            if result:
                messagebox.showinfo("Sucesso", "Logado com sucesso! Bem vindo")
                self.master.destroy()
                app = tk.Tk()
                app.title("Adega Olaria System")
                Application(app)
                app.geometry("1280x720")
                app.mainloop()
            else:
                messagebox.showerror("Erro", "Login ou senha incorretos!")
        except sqlite3.Error as e:
            messagebox.showerror("Erro", f"Erro ao executar consulta: {e}")







def logging():
    if __name__ == "__main__":
        app = tk.Tk()
        app.title("Adega Olaria System")
        Logger(app)
        app.geometry("300x200")
        app.mainloop()


logging()










