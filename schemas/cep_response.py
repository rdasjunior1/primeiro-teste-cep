from pydantic import BaseModel
from typing import Optional

class CepResponse(BaseModel):
    cep: str
    logradouro: Optional[str] = ""
    complemento: Optional[str] = ""
    bairro: Optional[str] = ""
    localidade: Optional[str] = ""
    uf: Optional[str] = ""
    ibge: Optional[str] = ""
    gia: Optional[str] = ""
    ddd: Optional[str] = ""
    siafi: Optional[str] = ""
    fonte: str
    