from flask import Flask, jsonify, request, render_template
from contato import Contato
import banco

# Inicializa o Flask
app = Flask(__name__)

# Cria a tabela de contatos se não existir
banco.criar_tabela()

# Rota para a página inicial


@app.route('/')
def index():
    return render_template('index.html')  # Renderiza o template HTML

# Rota para listar contatos


@app.route('/api/contatos', methods=['GET'])
def get_contatos():

    contatos = banco.listar_contatos()
    return jsonify([
        {"id": contato[0], "nome": contato[1],
            "telefone": contato[2], "email": contato[3]}
        for contato in contatos
    ])

# Rota para adicionar contato


@app.route('/api/contatos', methods=['POST'])
def add_contato():
    data = request.json
    contato = Contato(data.get['nome'],
                      data.get['telefone'],
                      data.get['email'], "")
    banco.adicionar_contato(contato)
    return jsonify({"message": "Contato adicionado com sucesso!"}), 201


# Rota para atualizar contato
@app.route('/api/contatos/<int:id>', methods=['PUT'])
def update_contato(id):
    data = request.json
    contato = Contato(data.get('nome'),
                      data.get('telefone'),
                      data.get('email'))
    banco.atualizar_contato(id, contato)
    return jsonify({"message": "Contato atualizado com sucesso!"})

# Rota para remover contato


@app.route('/api/contatos/<int:id>', methods=['DELETE'])
def delete_contato(id):
    banco.remover_contato(id)
    return jsonify({"message": "Contato removido com sucesso!"})


# Inicia o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
