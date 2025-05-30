"""API para consultar CEPs utilizando a API do ViaCEP com autenticação via token."""
from fastapi import FastAPI, Request, HTTPException
import requests

app = FastAPI()

TOKEN = "cavalo branco"

@app.get("/cep/{cep}")
def consultar_cep(cep: str, request: Request):
    
    """Consulta informações de endereço a partir do CEP informado.
    Requer token de autenticação via header."""
    
    auth = request.headers.get("Authorization")
    if not auth or auth != f"Bearer {TOKEN}":
        raise HTTPException(status_code=401, detail="Não autorizado")

    response = requests.get(f"https://viacep.com.br/ws/{cep}/json/", timeout=5)

    if response.status_code == 400 or "erro" in response.text:
        raise HTTPException(status_code=404, detail="CEP não encontrado")

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Erro ao consultar o ViaCEP")

    return response.json()
