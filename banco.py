import sqlite3


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
