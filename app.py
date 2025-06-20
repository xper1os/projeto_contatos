from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)


def conectar():
    """Conecta ao banco de dados SQLite e retorna a conexão."""
    conexao = sqlite3.connect('contatos.db')
    return conexao


def criar_tabela():
    """Cria a tabela de contatos no banco de dados, se não existir."""
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL,
            telefone TEXT NOT NULL
        )
    ''')
    conexao.commit()
    conexao.close()


def adicionar_contato(nome, email, telefone):
    """Adiciona um novo contato ao banco de dados."""
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
        INSERT INTO contatos (nome, email, telefone)
        VALUES (?, ?, ?)
    ''', (nome, email, telefone))
    conexao.commit()
    conexao.close()


def listar_contatos():
    """Lista todos os contatos do banco de dados."""
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM contatos')
    contatos = cursor.fetchall()
    conexao.close()
    return contatos


def atualizar_contato(id, nome, email, telefone):
    """Atualiza um contato existente no banco de dados."""
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
        UPDATE contatos
        SET nome = ?, email = ?, telefone = ?
        WHERE id = ?
    ''', (nome, email, telefone, id))
    conexao.commit()
    conexao.close()


def remover_contato(id):
    """Remove um contato do banco de dados."""
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute('''
        DELETE FROM contatos
        WHERE id = ?
    ''', (id,))
    conexao.commit()
    conexao.close()


criar_tabela()


@app.route('/')
def index():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
      <meta charset="UTF-8">
      <title>Gerenciador de Contatos</title>
      <script>
        async function carregarContatos() {
          const res = await fetch("/api/contatos");
          const contatos = await res.json();
          const lista = document.getElementById("lista-contatos");
          lista.innerHTML = "";
          contatos.forEach(c => {
            const li = document.createElement("li");
            li.innerHTML = `
              ${c.nome} - ${c.telefone} - ${c.email}
              <button onclick="editarContato(${c.id}, '${c.nome}', '${c.telefone}', '${c.email}')">Editar</button>
              <button onclick="removerContato(${c.id})">Excluir</button>
            `;
            lista.appendChild(li);
          });
        }

        async function removerContato(id) {
          await fetch("/api/contatos/" + id, { method: "DELETE" });
          carregarContatos();
        }

        function editarContato(id, nome, telefone, email) {
          document.getElementById("contato-id").value = id;
          document.getElementById("nome").value = nome;
          document.getElementById("telefone").value = telefone;
          document.getElementById("email").value = email;
        }

        document.addEventListener("DOMContentLoaded", () => {
          document.getElementById("form-contato").addEventListener("submit", async e => {
            e.preventDefault();
            const id = document.getElementById("contato-id").value;
            const nome = document.getElementById("nome").value;
            const telefone = document.getElementById("telefone").value;
            const email = document.getElementById("email").value;
            const dados = { nome, telefone, email };
            if (id) {
              await fetch("/api/contatos/" + id, {
                method: "PUT",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(dados)
              });
            } else {
              await fetch("/api/contatos", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(dados)
              });
            }
            document.getElementById("form-contato").reset();
            document.getElementById("contato-id").value = "";
            carregarContatos();
          });
          carregarContatos();
        });
      </script>
    </head>
    <body>
      <h1>Gerenciador de Contatos</h1>
      <form id="form-contato">
        <input type="hidden" id="contato-id">
        <input type="text" id="nome" placeholder="Nome" required>
        <input type="text" id="telefone" placeholder="Telefone">
        <input type="email" id="email" placeholder="Email">
        <button type="submit">Salvar</button>
      </form>
      <ul id="lista-contatos"></ul>
    </body>
    </html>
    """)
