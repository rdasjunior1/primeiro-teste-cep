from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from routers import ceps
import os

# carrega as variáveis de ambiente do .env
load_dotenv()

api_token = os.getenv("API_TOKEN")

# Verifica se o token foi carregado
if not api_token:
    raise ValueError("API_TOKEN não definido no arquivo .env")

# Instância do FastAPI
app = FastAPI()

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Importa e inclui as rotas
from routers import ceps
app.include_router(ceps.router, prefix="/cep")

@app.get("/")
def root():
    return {"mensagem": "API do ViaCep funcionando"}
