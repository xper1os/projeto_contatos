import os
from flask import Flask, jsonify, request, render_template
from contato import Contato
import banco

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'frontend', 'templates'),
    static_folder=os.path.join(BASE_DIR, 'frontend', 'static')
)


banco.criar_tabela()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/contatos', methods=['GET'])
def get_contatos():
    contatos = banco.listar_contatos()
    return jsonify([
        {"id": contato[0], "nome": contato[1], "telefone": contato[2], "email": contato[3]}
        for contato in contatos
    ])


@app.route('/api/contatos', methods=['POST'])
def add_contato():
    data = request.json
    contato = Contato(data.get('nome'), data.get('telefone'), data.get('email'))
    banco.adicionar_contato(contato)
    return jsonify({"message": "Contato adicionado com sucesso!"}), 201


@app.route('/api/contatos/<int:id>', methods=['PUT'])
def update_contato(id):
    data = request.json
    contato = Contato(data.get('nome'), data.get('telefone'), data.get('email'))
    banco.atualizar_contato(id, contato)
    return jsonify({"message": "Contato atualizado com sucesso!"})


@app.route('/api/contatos/<int:id>', methods=['DELETE'])
def delete_contato(id):
    banco.remover_contato(id)
    return jsonify({"message": "Contato removido com sucesso!"})


if __name__ == '__main__':
    app.run(debug=True)
