import sqlite3

DATABASE_NAME = "avicola.db"

def get_conn():
    # 1 - Abrir a conexão
    conn = sqlite3.connect(DATABASE_NAME)
    return conn