import sqlite3

def get_classificacao():
    conn = sqlite3.connect('classificacao.db')
    cur = conn.cursor()
    cur.execute("SELECT time, pontos FROM classificacao ORDER BY pontos DESC")
    dados = cur.fetchall()
    conn.close()
    return dados
