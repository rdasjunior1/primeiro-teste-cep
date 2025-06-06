from fastapi import APIRouter, Depends
from schemas.cep_response import CepResponse
from bussines.bussines_ceps import CepService
from dependencies import get_token
import os

router = APIRouter()

@router.get("/{cep}", response_model=CepResponse, dependencies=[Depends(get_token)])
async def get_cep(cep: str):
    return await CepService.buscar_cep(cep)
