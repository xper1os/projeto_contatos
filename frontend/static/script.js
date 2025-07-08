document.addEventListener("DOMContentLoaded", carregarContatos);

async function carregarContatos() {
    const res = await fetch("/api/contatos");
    const contatos = await res.json();
    const lista = document.getElementById("listar-contatos");
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

document.getElementById("form-contato").addEventListener("submit", async function (e) {
    e.preventDefault();
    await salvarContato();
});

async function salvarContato() {
    const id = document.getElementById("contato-id").value;
    const nome = document.getElementById("nome").value;
    const telefone = document.getElementById("telefone").value;
    const email = document.getElementById("email").value;

    const payload = { nome, telefone, email };

    if (id) {
        await fetch(`/api/contatos/${id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });
    } else {
        await fetch("/api/contatos", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload)
        });
    }

    limparCampos();
    carregarContatos();
}

function editarContato(id, nome, telefone, email) {
    document.getElementById("contato-id").value = id;
    document.getElementById("nome").value = nome;
    document.getElementById("telefone").value = telefone;
    document.getElementById("email").value = email;
}

async function removerContato(id) {
    await fetch(`/api/contatos/${id}`, { method: "DELETE" });
    carregarContatos();
}

function limparCampos() {
    document.getElementById("contato-id").value = "";
    document.getElementById("nome").value = "";
    document.getElementById("telefone").value = "";
    document.getElementById("email").value = "";
}
