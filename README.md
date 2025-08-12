# 🚗 API Flask de Carros

Uma API simples para gerenciar informações de carros, desenvolvida em **Flask** e **SQLAlchemy**, com banco de dados **SQLite**.

---

## 📌 Tabela de Conteúdos
- [Funcionalidades](#-funcionalidades)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Como Executar o Projeto](#-como-executar-o-projeto)
- [Endpoints da API](#-endpoints-da-api)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Próximos Passos](#-próximos-passos)
- [Contribuição](#-contribuição)

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
## 🔌 Endpoints da API

### **Listar todos os carros**
`GET /carros`

**Descrição:**  
Retorna todos os carros cadastrados no banco de dados.

**Exemplo de resposta (200 OK):**
```json
[
    {
        "id": 1,
        "marca": "Fiat",
        "modelo": "Marea",
        "ano": 1999
    },
    {
        "id": 2,
        "marca": "Volkswagen",
        "modelo": "Gol",
        "ano": 2020
    }
]
```
### **Cadastrar novo carro**
`POST /carros`
**Parâmetros (Body - JSON):**
```json
{
    "marca": "string (obrigatório)",
    "modelo": "string (obrigatório)",
    "ano": "integer (opcional)"
}
```
**Exemplo de requisição:**
```json
{
    "marca": "Toyota",
    "modelo": "Corolla",
    "ano": 2022
}
```
**Respostas possíveis:**
`201 Created` (Sucesso)
```json
{
    "id": 3,
    "marca": "Toyota",
    "modelo": "Corolla",
    "ano": 2022
}
```
`400 Bad Request` (Se faltar campo obrigatório)
```json
{
    "erro": "Os campos 'marca' e 'modelo' são obrigatórios"
}
```
**Formato Resumido**
| Método | Endpoint   | Descrição               | Body (Exemplo)                          |
|--------|-----------|-------------------------|-----------------------------------------|
| GET    | `/carros` | Lista todos os carros    | -                                       |
| POST   | `/carros` | Cadastra novo carro      | `{"marca": "Fiat", "modelo": "Marea"}` |

## 📂 Estrutura do Projeto
```text
flask-api-carros/
├── app/
│   ├── __init__.py       # Configuração do Flask e banco de dados
│   ├── models.py         # Modelo `Carro` (SQLAlchemy)
│   └── routes.py         # Rotas da API
├── instance/
│   └── storage.db        # Banco de dados SQLite (gerado automaticamente)
├── main.py               # Ponto de entrada da aplicação
├── README.md             # Este arquivo
└── requirements.txt      # Dependências do projeto
```
**🔜 Próximos Passos**
- Adicionar autenticação JWT
- Implementar DELETE e PUT para editar/excluir carros
- Migrar para MySQL/PostgreSQL
- Configurar Docker para deploy
