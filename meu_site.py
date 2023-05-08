from flask import Flask, render_template, jsonify, request
import json
import jinja2

app = Flask(__name__)

# Carrega os dados do arquivo JSON na variável "dados"
with open("foodlist.json", 'r', encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

#retorna lista de itens para o menu
def ListaItens():
    l = [(str(row["id"]), row["description"]) for row in dados]
    return l 

# Retorna o alimento com o ID fornecido ou None se não encontrado
def buscar_por_id(id_busca):
    for alimento in dados:
        if alimento['id'] == id_busca:
            return alimento
    return None

@app.route('/')
def index():
    # Gera uma lista de itens a partir dos dados carregados do arquivo JSON
    lista = ListaItens()
    return render_template('homepage.html', lista=lista)


@app.route('/buscar_alimento', methods=['POST'])
def buscar_alimento():
    id_busca = int(request.form['opcao'])
    alimento = buscar_por_id(id_busca)
    print(id_busca)
    print(alimento)
    return render_template('resultado.html', alimento=alimento)
    


if __name__ == '__main__':
    app.run(debug=True)
