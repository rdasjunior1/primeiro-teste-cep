from fastapi import APIRouter, Header, HTTPException
from typing import Annotated
from schemas.cep_response import CepResponse
from bussines.bussines_ceps import buscar_cep
import os

router = APIRouter()  

@router.get("/{cep}", response_model=CepResponse)
def get_cep(cep: str, authorization: Annotated[str, Header()] = ""):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Token inválido")
    
    token = authorization.split(" ")[1]
    if token != os.getenv("API_TOKEN"):
        raise HTTPException(status_code=401, detail="Token inválido")
    
    return buscar_cep(cep)