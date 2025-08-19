# 🚗 API Flask de Carros

Uma API simples para gerenciar informações de carros, desenvolvida em **Flask** e **SQLAlchemy**, com banco de dados **SQLite**.

---

## 📌 Tabela de Conteúdos

- [🚗 API Flask de Carros](#-api-flask-de-carros)
  - [📌 Tabela de Conteúdos](#-tabela-de-conteúdos)
  - [🛠 Funcionalidades](#-funcionalidades)
  - [💻 Tecnologias Utilizadas](#-tecnologias-utilizadas)
  - [🚀 Como Executar o Projeto](#-como-executar-o-projeto)
    - [**Pré-requisitos**](#pré-requisitos)
    - [**Passo a Passo**](#passo-a-passo)
  - [🔐 Autenticação JWT](#-autenticação-jwt)
  - [Variáveis de Ambiente:](#variáveis-de-ambiente)
  - [🔌 Endpoints da API](#-endpoints-da-api)
  - [📂 Estrutura do Projeto](#-estrutura-do-projeto)

---

## 🛠 Funcionalidades
✅ **Listar todos os carros** (`GET /carros`)  
✅ **Cadastrar novo carro** (`POST /carros`)  
✅ **Banco de dados SQLite** (Fácil configuração)  
✅ **Pronto para Docker** (Configuração futura)

---

## 💻 Tecnologias Utilizadas
- **Python** (Linguagem principal)
- **Flask** (Framework web)
- **Flask-SQLAlchemy** (ORM para banco de dados)
- **SQLite** (Banco de dados local)

---

## 🚀 Como Executar o Projeto

### **Pré-requisitos**
- Python 3.8+
- Pip (Gerenciador de pacotes)

### **Passo a Passo**
1. **Clone o repositório**
   ```bash
   git clone https://github.com/seu-usuario/flask-api-carros.git
   cd flask-api-carros
   ```
2. **Crie um ambiente virtual (opcional, mas recomendado)**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate    # Windows
    ```
3. **Instale as dependências**
    ```bash
    pip install -r requirements.txt
    ```
4. **Execute a aplicação**
    ```bash
    python main.py
    ```
5. **Acesse a API**
- Abra o navegador ou use Postman/Insomnia em:
  ```text
  http://localhost:5000/carros
  ```

## 🔐 Autenticação JWT
1. **Registrar usuário** → `/register`
2. **Fazer login** → `/login` (obtém token JWT)
3. **Usar token em requisições protegidas** → Authorization: Bearer <token>

## Variáveis de Ambiente:
**Crie um arquivo** `.env` na raiz do projeto:
```env
JWT_SECRET_KEY=sua_chave_super_secreta_aqui_32_caracteres
JWT_ACCESS_TOKEN_EXPIRES=3600
```

## 🔌 Endpoints da API

<<<<<<< HEAD
**🔐 Autenticação**
| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|---------------|
| POST | `/register` |	Registrar novo usuário | ❌ |
| POST | `/login` |	Fazer login | ❌ |
| GET | `/profile` |	Ver perfil do usuário | ✅ |

**🚗 Carros (Protegidos por JWT)**
| Método | Endpoint   | Descrição               | Autenticação |
|--------|-----------|-------------------------|---------------|
| GET    | `/carros` | Lista todos os carros | ✅ |
| POST   | `/carros` | Cadastra novo carro | ✅ |
| GET   | `/carros/<id>` | Buscar carro por ID | ✅ |
| PUT   | `/carros/<id>` | Atualizar carro (completo) |  ✅ |
| PATCH   | `/carros/<id>` | Atualizar carro (parcial) | ✅ |
| DELETE   | `/carros/<id>` | Deletar carro | ✅ |

## 📂 Estrutura do Projeto
```text
flask-api-carros/
├── app/
│   ├── __init__.py          # Configuração do Flask e extensões
│   ├── models.py            # Modelos: User e Carro
│   ├── routes.py            # Rotas de carros (protegidas)
│   └── auth_routes.py       # Rotas de autenticação
├── instance/
│   └── storage.db           # Banco de dados SQLite (auto-gerado)
├── .env                     # Variáveis de ambiente (JWT)
├── main.py                  # Ponto de entrada da aplicação
├── requirements.txt         # Dependências do projeto
└── README.md               # Documentação
```
**🔜 Próximos Passos**

- Migrar para MySQL/PostgreSQL
- Configurar Docker para deploy
