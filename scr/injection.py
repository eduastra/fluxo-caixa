import sqlite3

conn = sqlite3.connect('user_data.db')
cursor = conn.cursor()

# Criar a tabela 'users' se ela não existir
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                   (login TEXT PRIMARY KEY, password TEXT, age INTEGER)''')

# Adicionar alguns dados de exemplo para a tabela 'users'
cursor.execute("INSERT INTO users (login, password) VALUES (?, ?)",
               ("", ""))

# Salvar as alterações no banco de dados
conn.commit()

# Consultar e exibir os registros da tabela 'users'
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Fechar a conexão com o banco dedos da
conn.close()



def connect_to_database():
    # Conecte-se ao banco de dados warehouse.db (ou crie um novo se não existir)
    connection = sqlite3.connect("warehouse.db")

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

    # Faça commit das alterações e feche a conexão
    connection.commit()
    connection.close()