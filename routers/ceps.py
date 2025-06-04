from fastapi import APIRouter, Header, HTTPException
from typing import Annotated
from schemas.cep_response import CepResponse
from bussines.bussines_ceps import buscar_cep
from fastapi import APIRouter, Depends
from dependencies import get_token
import os

router = APIRouter()

@router.get("/{cep}", response_model=CepResponse)
async def get_cep(cep: str, token: str = Depends(get_token)):
    return await buscar_cep(cep)
