import sqlite3
import json

def get_classificacao():
    conn = sqlite3.connect('classificacao.db')
    conn.row_factory = sqlite3.Row  
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            id,
            grupo AS group,
            jogador_casa AS homePlayer,
            atletica_casa AS homeClub,
            jogador_fora AS awayPlayer,
            atletica_fora AS awayClub,
            pontos_casa AS homeScore,
            pontos_fora AS awayScore,
            data_hora AS datetime
        FROM partidas
        ORDER BY datetime ASC
    """)
    
    rows = cur.fetchall()
    conn.close()

    resultado = []
    for row in rows:
        match = {
            "id": row["id"],
            "group": row["group"],
            "homePlayer": row["homePlayer"],
            "homeClub": row["homeClub"],
            "awayPlayer": row["awayPlayer"],
            "awayClub": row["awayClub"],
            "homeScore": row["homeScore"],
            "awayScore": row["awayScore"],
            "datetime": row["datetime"],  
        }
        resultado.append(match)

    return resultado
