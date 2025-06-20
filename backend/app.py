import sqlite3

def conectar():
    return sqlite3.connect("contatos.db")

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contatos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT,
            email TEXT
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_contato(contato):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO contatos (nome, telefone, email) VALUES (?, ?, ?)",
        (contato.nome, contato.telefone, contato.email)
    )
    conn.commit()
    conn.close()

def listar_contatos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contatos")
    contatos = cursor.fetchall()
    conn.close()
    return contatos

def atualizar_contato(id, contato):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE contatos SET nome = ?, telefone = ?, email = ? WHERE id = ?",
        (contato.nome, contato.telefone, contato.email, id)
    )
    conn.commit()
    conn.close()

def remover_contato(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contatos WHERE id = ?", (id,))
    conn.commit()
    conn.close()
