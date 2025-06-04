# 🚀 Projeto FastAPI - Consulta de CEP com Autenticação

Este é um projeto em FastAPI que expõe um endpoint para consulta de CEPs utilizando duas APIs públicas (ViaCEP e BrasilAPI). O sistema inclui autenticação por token, tratamento de erros, boas práticas de código e documentação.

---

## ✅ Funcionalidades

- 🔐 Autenticação por token (via header `Authorization`)
- 🔎 Consulta de CEP via **ViaCEP** e **BrasilAPI**
- 📌 Seleciona automaticamente a resposta mais rápida
- ⚠️ Tratamento de erros e CEPs inválidos
- 🧪 Testes no Postman incluídos
- 📚 Documentação gerada automaticamente via Swagger

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- FastAPI
- Uvicorn
- HTTPx
- Pydantic
- Python-dotenv
- Pylint

---

## 🚧 Estrutura do Projeto