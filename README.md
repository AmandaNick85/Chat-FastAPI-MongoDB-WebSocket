# 💬 FastAPI Chat + MongoDB + WebSocket
<<<<<<< HEAD

=======
Trabalho avaliativo2 para P1 de banco de dados não relacional, criando um chat em tempo real com FastAPI.
>>>>>>> 9eae65b6c3b70465fc97c7ec77022679ec47cce1
Chat em tempo real usando **FastAPI**, **WebSockets** e **MongoDB Atlas**.
Permite múltiplos usuários se conectarem em salas diferentes e envia mensagens instantaneamente.

---

## 🛠️ Pré-requisitos

- Python 3.10+ instalado
- Conta no [MongoDB Atlas](https://cloud.mongodb.com/)
- VSCode (recomendado)
- Navegador moderno (Chrome, Edge, Firefox, etc.)

---

## ⚙️ Passos para rodar localmente

### 1. Crie seu cluster no MongoDB Atlas

- Vá até: https://cloud.mongodb.com
- Crie um banco (cluster gratuito)
- Em **Database Access**, crie um usuário e senha
- Em **Network Access**, adicione seu IP ou `0.0.0.0/0` (para testes)
- Copie a **Connection String** (ex: `mongodb+srv://...`)

### 2. Configure o `.env`

Crie um arquivo `.env` na raiz do projeto (mesmo nível de `requirements.txt`) com:

```env
MONGO_URL=<sua_mongodb_atlas_connection_string>
MONGO_DB=chatdb

###  Crie e ative a virtualenv

**Windows (Powershell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux/Mac:**

```bash
python3 -m venv venv
source venv/bin/activate
```
---
###  Instale as dependências

```bash
pip install -r requirements.txt
```
---

###  Rode o servidor

```bash
uvicorn app.main:app --reload
```
---

###  Acesse o chat

Abra no navegador:

```
http://127.0.0.1:8000
```

---

## 📂 Estrutura do projeto

```
app/
├── main.py              # Ponto de entrada da aplicação
├── database.py          # Conexão e funções com MongoDB
├── models.py            # Schemas Pydantic para validação
├── ws_manager.py        # Gerenciamento de WebSockets
├── .env
├── routes/messages.py   # Rotas de API (caso necessário)
└── static/
    ├── index.html       # Interface do chat
    └── styles.css       # Estilo do chat
requirements.txt
README.md
```

---

## 💻 Funcionalidades

* Chat em tempo real com **WebSockets**
* Salas de chat independentes
* Histórico das últimas mensagens carregadas ao entrar
* Layout simples e responsivo

---

## 🔧 Tecnologias

* **FastAPI** – Framework web assíncrono em Python
* **MongoDB Atlas** – Banco de dados NoSQL na nuvem
* **Motor** – Driver assíncrono do MongoDB
* **WebSockets** – Comunicação bidirecional em tempo real
* **HTML / CSS** – Interface do chat

<<<<<<< HEAD
---
=======
---
>>>>>>> 9eae65b6c3b70465fc97c7ec77022679ec47cce1
