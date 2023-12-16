import sqlite3
import datetime


def itens():
    # Conecte-se ao banco de dados warehouse.db (ou crie um novo se não existir)
    connection = sqlite3.connect("warehouse.db")
    data_atual = datetime.datetime.now().strftime('%Y-%m-%d')

    # Crie a tabela itens se ela ainda não existir
    cursor = connection.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS itens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item TEXT NOT NULL,
        quantidade INTEGER NOT NULL,
        data TEXT NOT NULL
    )
    """)
    cursor.execute("""
    INSERT INTO itens (id, item, quantidade, data)
    VALUES (?, ?, ?, ?)
    """, (1, 'whisky', 10, data_atual))
    cursor.execute("""
    INSERT INTO itens (id, item, quantidade, data)
    VALUES (?, ?, ?, ?)
    """, (2, 'vodka', 10, data_atual))
    cursor.execute("""
    INSERT INTO itens (id, item, quantidade, data)
    VALUES (?, ?, ?, ?)
    """, (3, 'whisky', 2, data_atual))
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sales (
        item TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        payment_method TEXT NOT NULL,
        date TEXT NOT NULL,
        user TEXT NOT NULL
    )
    """)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS entries (
        item TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        date TEXT NOT NULL
    )
    """)


        # Criar a tabela 'users' se ela não existir
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                    (login TEXT PRIMARY KEY, password TEXT, age INTEGER)''')

    # Adicionar alguns dados de exemplo para a tabela 'users'
    cursor.execute("INSERT INTO users (login, password) VALUES (?, ?)",
                ("", ""))
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pricing (
        item TEXT NOT NULL,
        price FLOAT NOT NULL,
        date TEXT
    )
    """)
    

    # Faça commit das alterações e feche a conexão
    connection.commit()
    connection.close()


itens()
    
print("foi")