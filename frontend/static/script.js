

async function carregarContatos() {
    try {
        const response = await fetch('/api/contatos');
        const data = await response.json();
        const listaContatos = document.getElementById('listar_contatos');
        listaContatos.innerHTML = '';
        data.forEach(contato => {
            const li = document.createElement('li');
            li.textContent = `${contato.nome} - ${contato.telefone} - ${contato.email}`;
            <button onclick="editarContato(${contato.id}, '${contato.nome}', '${contato.telefone}', '${contato.email}')">Editar</button>;
            <button onclick="excluirContato(${contato.id})">Excluir</button>
            listaContatos.appendChild(li);
        });
    } catch (error) {
        console.error('Erro ao carregar contatos:', error);
    }
}

async function removerContato(id) {
    try {
        const response = await fetch(`/api/contatos/${id}`, {
            method: 'DELETE'
        });
        if (response.ok) {
            carregarContatos();
        } else {
            console.error('Erro ao excluir contato:', response.statusText);
        }
    } catch (error) {
        console.error('Erro ao excluir contato:', error);
    }
}

function editarContato(id, nome, telefone, email) {
    document.getElementById('contato-id').value = id;
    document.getElementById('nome').value = nome;
    document.getElementById('telefone').value = telefone;
    document.getElementById('email').value = email;
}

document.getElementById('form-contato').addEventListener('submit', async e => {
    e.preventDefault();
    const id = document.getElementById('contato-id').value;
    const nome = document.getElementById('nome').value;
    const telefone = document.getElementById('telefone').value;
    const email = document.getElementById('email').value;
    const dados = {nome, telefone, email };

    if (id) {
        // Atualizar contato existente
        await fetch(`/api/contatos/${id}`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dados)
        });
    }
    else {
        // Adicionar novo contato
        await fetch('/api/contatos', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dados)
        });
    }
    document.getElementById('form-contato').reset();
    document.getElementById('contato-id').value = '';
});
carregarContatos();