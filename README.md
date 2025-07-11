
# 📇 projeto_contatos

Aplicação web simples e completa (back-end + front-end) para **gerenciar contatos**, com funcionalidades de cadastro, listagem, edição e exclusão em tempo real.

---

## 🔧 Tecnologias Utilizadas

- 🐍 **Python 3 + Flask** – Back-end leve e rápido usando API REST
- 🗃️ **SQLite** – Banco de dados local simples e integrado
- 🌐 **HTML + JavaScript (Fetch API)** – Front-end com consumo de API sem frameworks

---

## 🚀 Funcionalidades

- ✅ Cadastrar novos contatos
- 📄 Listar todos os contatos salvos
- ✏️ Editar contatos existentes
- ❌ Excluir contatos individualmente
- 🔄 Atualização dinâmica com JavaScript (sem recarregar a página)
- 🖥️ Interface responsiva e leve

---

## 📁 Estrutura do Projeto

```

projeto_contatos/
│
├── backend/                     # Código do servidor e banco
│   ├── app.py                   # Servidor principal Flask + rotas da API
│   ├── banco.py                 # Lógica do banco de dados (conexão, CRUD)
│   ├── contatos.db              # Banco de dados SQLite (criado automaticamente)
│   └── requirements.txt         # Dependências do back-end
│
├── frontend/                    # Interface web
│   ├── templates/
│   │   └── index.html           # Página principal HTML
│   └── static/
│       └── script.js            # Código JS que consome a API via fetch()
│
├── consultar.py                 # Script auxiliar para listar contatos no terminal
└── README.md                    # Documentação do projeto

````

---

## ⚙️ Como Rodar o Projeto Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/gerenciador_de_contatos.git
cd gerenciador_de_contatos/backend
````

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

> 💡 **Dica:** Para isolar dependências, use um ambiente virtual:
>
> ```bash
> python -m venv venv
> venv\Scripts\activate  # no Windows
> ```

### 3. Inicie o servidor Flask

```bash
python app.py
```

Acesse a aplicação no navegador em:

```
http://127.0.0.1:5000
```

---

## 🧪 Consulta rápida via terminal

Você pode rodar um script auxiliar para listar os contatos diretamente no terminal, sem usar o navegador:

```bash
python consultar.py
```

---

## 🧠 APIs Disponíveis

| Método | Rota                 | Descrição                     |
| ------ | -------------------- | ----------------------------- |
| GET    | `/api/contatos`      | Lista todos os contatos       |
| POST   | `/api/contatos`      | Cria um novo contato          |
| PUT    | `/api/contatos/<id>` | Atualiza um contato existente |
| DELETE | `/api/contatos/<id>` | Remove um contato do banco    |

As APIs trocam dados no formato JSON e são consumidas pelo front-end em tempo real.

---

## 📌 Observações

* O banco `contatos.db` será criado automaticamente na primeira execução
* Todos os arquivos do front-end estão em `frontend/templates/` e `frontend/static/`
* O projeto pode ser facilmente estendido com Bootstrap, React ou deploy em serviços como Render/Heroku

