from flask import Flask, request, jsonify
import sqlite3
from models import get_classificacao

app = Flask(__name__)

def criar_tabela():
    conn = sqlite3.connect('classificacao.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS partidas (
            id TEXT PRIMARY KEY,
            grupo TEXT,
            jogador_casa TEXT,
            atletica_casa TEXT,
            jogador_fora TEXT,
            atletica_fora TEXT,
            pontos_casa INTEGER,
            pontos_fora INTEGER,
            data_hora TEXT
        )
    ''')
    conn.commit()
    conn.close()

criar_tabela()

@app.route('/', methods=['POST'])
def create_match():
    try:
        match_data = request.get_json()

        required_keys = (
            'id', 'group', 'homePlayer', 'homeClub',
            'awayPlayer', 'awayClub', 'homeScore',
            'awayScore', 'datetime'
        )

        if not all(key in match_data for key in required_keys):
            return jsonify({"error": "Faltando dados obrigatórios"}), 400

        conn = sqlite3.connect('classificacao.db')
        cur = conn.cursor()

        cur.execute('''
            INSERT INTO partidas (
                id, grupo, jogador_casa, atletica_casa,
                jogador_fora, atletica_fora, pontos_casa,
                pontos_fora, data_hora
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            match_data['id'],
            match_data['group'],
            match_data['homePlayer'],
            match_data['homeClub'],
            match_data['awayPlayer'],
            match_data['awayClub'],
            match_data['homeScore'],
            match_data['awayScore'],
            match_data['datetime']
        ))

        conn.commit()
        conn.close()

        return jsonify({"mensagem": "Partida registrada com sucesso!"}), 201

    except sqlite3.IntegrityError:
        return jsonify({"error": "Já existe uma partida com esse ID"}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_matches', methods=['GET'])
def get_matches():
    try:
        dados = get_classificacao()
        return jsonify(dados), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
