from flask import Flask, render_template
from models import getClassificacao

app = Flask(name)

@app.rout('/')
def home():
    tabela = classifica()
    return render_template('classificacao.html',tabela = tabela)

if __name__ == '__main__':
    app.run(debug=True)