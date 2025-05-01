from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor funcionando! Acesse /matches para interagir."

@app.route('/matches', methods=['POST'])
def create_match():
    try:
        match_data = request.get_json()

        if not all(key in match_data for key in ('id', 'group', 'homePlayer', 'homeClub', 'awayPlayer', 'awayClub', 'homeScore', 'awayScore', 'datetime')):
            return jsonify({"error": "Faltando dados obrigatórios"}), 400

        return jsonify(match_data), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
