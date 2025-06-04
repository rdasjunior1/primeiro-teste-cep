# 🔍 Consulta de CEP com FastAPI

Este projeto é uma API REST desenvolvida com **FastAPI** que permite consultar dados de um CEP utilizando múltiplos serviços externos (como ViaCEP e BrasilAPI), com autenticação via token, tratamento de erros, e boas práticas de organização.

## 📦 Funcionalidades

- Consulta de CEPs por meio de múltiplas APIs externas.
- Retorno rápido usando chamadas assíncronas concorrentes.
- Autenticação por token via header (`Authorization`).
- Tratamento de erros para CEPs inválidos ou APIs indisponíveis.
- Estrutura modular com pastas organizadas por responsabilidade.
- Configuração via variáveis de ambiente.
- Testes manuais via Postman.

## 🛠️ Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [httpx](https://www.python-httpx.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/)
- Python 3.10+

## ▶️ Como executar localmente

1. **Clone o repositório:**

```bash
git clone https://github.com/rdasjunior1/primeiro-teste-cep.git
cd primeiro-teste-cep

2-Crie e ative um ambiente virtual:

bash
Copiar
Editar
python3 -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate

3- Instale as dependências:

bash
Copiar
Editar
pip install -r requirements.txt
Configure as variáveis de ambiente (opcional):

4- você pode criar um arquivo .env com a seguinte variável:

env
Copiar
Editar
TOKEN=seu_token_aqui

5- Execute o servidor:

bash
Copiar
Editar
uvicorn main:app --reload
🔐 Autenticação


A API requer o envio de um token no header da requisição:

makefile
Copiar
Editar
Authorization: Bearer seu_token_aqui
📮 Endpoint
GET /cep/{cep}
Consulta dados de um CEP.
Exemplo: /cep/01001000

Resposta de Sucesso:
json
Copiar
Editar
{
  "cep": "01001-000",
  "logradouro": "Praça da Sé",
  "bairro": "Sé",
  "cidade": "São Paulo",
  "estado": "SP",
  "origem": "viacep"
}
Respostas de Erro:
400: CEP inválido.

401: Token ausente ou inválido.

404: Nenhuma API respondeu com dados válidos.

500: Erro interno do servidor.

📁 Estrutura do Projeto
bash
Copiar
Editar
.
├── bussines/           # Lógica de negócio
├── client/             # Clientes de APIs externas
├── routers/            # Rotas da aplicação
├── schemas/            # Schemas do Pydantic
├── dependencies.py     # Funções auxiliares (ex: auth)
├── settings.py         # Configurações do sistema
├── main.py             # Ponto de entrada da aplicação
├── requirements.txt    # Dependências do projeto
└── README.md
🧪 Testes
Os testes manuais podem ser realizados com o Postman, usando o endpoint /cep/{cep} e incluindo o token no header.

📤 Publicação
O projeto está disponível no GitHub:
👉 https://github.com/rdasjunior1/primeiro-teste-cep

👨‍💻 Autor
Raildo Júnior – Desenvolvedor Júnior