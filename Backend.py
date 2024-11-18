import sqlite3

# Conexão com o banco de dados SQLite
def connect():
    conn = sqlite3.connect("fans.db")
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS fan (
            id INTEGER PRIMARY KEY,
            name TEXT,
            surname TEXT,
            email TEXT,
            instagram TEXT
        )
    """)
    conn.commit()
    conn.close()

# Função para inserir um novo fã no banco de dados
def insert(name, surname, email, instagram):
    conn = sqlite3.connect("fans.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO fan (name, surname, email, instagram) VALUES (?, ?, ?, ?)", (name, surname, email, instagram))
    conn.commit()
    conn.close()

# Função para buscar fãs pelo nome
def search(name=""):
    conn = sqlite3.connect("fans.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM fan WHERE name LIKE ?", ('%' + name + '%',))
    rows = cur.fetchall()
    conn.close()
    return rows

# Função para visualizar todos os fãs cadastrados
def view_all():
    conn = sqlite3.connect("fans.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM fan")
    rows = cur.fetchall()
    conn.close()
    return rows

# Função para excluir um fã pelo ID
def delete_fan(fan_id):
    conn = sqlite3.connect("fans.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM fan WHERE id = ?", (fan_id,))
    conn.commit()
    conn.close()

# Função para salvar um novo fã (para ser chamada do GUI)
def save_fan(name, surname, email, instagram):
    insert(name, surname, email, instagram)

# Função para obter todos os fãs (pode ser usada para atualizar uma listbox, por exemplo)
def get_fans():
    return view_all()

# Chama a função de conexão ao iniciar
connect()
