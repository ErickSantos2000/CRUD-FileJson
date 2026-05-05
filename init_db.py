import sqlite3
from helpers.database import get_conn as conexao

# nome do arquivo que representa o banco de dados
DATABASE_NAME = "avicola.db"

# inicia variavel de conexão 
conn = None

try:
    # cria um obj de conexão para se comunicar com o sqlite
    conn = conexao()

    # le o arquivo sql e executa os comandos para criar as tabelas
    with open('schema.sql') as f:
        conn.executescript(f.read())

    # confirma as alterações no banco de dados
    conn.commit
        
except Exception as e:
    print(e)

finally:
    if conn:
        conn.close