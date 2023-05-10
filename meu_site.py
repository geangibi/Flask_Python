from flask import Flask, render_template, jsonify, request
import json

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
    lista = ListaItens()
    return render_template('homepage.html', alimento=alimento, lista=lista)

@app.route('/lista_itens', methods=['GET', 'POST'])
def lista_itens():
    # Lista inicial de itens (pode ser carregada de um arquivo ou banco de dados)
    lista = [(str(row["id"]), row["description"]) for row in dados]

    if request.method == 'POST':
        # Se o método da requisição for POST, significa que o usuário adicionou um novo item
        novo_item = ListaItens()
        lista.append(novo_item)
    elif request.args.get('remover'):
        # Se o parâmetro 'remover' estiver presente na URL, significa que o usuário quer remover um item
        id_remover = int(request.args.get('remover'))
        lista = [item for item in lista if item[0] != str(id_remover)]

    return render_template('homepage.html', lista=lista)


if __name__ == '__main__':
    app.run(debug=True)