import sqlite3

def connect():
    return sqlite3.connect('vendas.db')

def init_db():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pedidos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            produto TEXT,
            valor REAL,
            status TEXT DEFAULT 'pendente',
            pref_id TEXT
        )
    ''')
    conn.commit()
    conn.close()

def salvar_pedido(user_id, produto, valor, pref_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO pedidos (user_id, produto, valor, pref_id) VALUES (?, ?, ?, ?)",
        (user_id, produto, valor, pref_id)
    )
    conn.commit()
    conn.close()
