from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

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
