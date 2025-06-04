from pydantic import BaseModel, Field
from typing import Optional

class CepResponse(BaseModel):
    cep: str
    logradouro: Optional[str] = Field(None, description="Logradouro (rua, avenida, etc)")
    complemento: Optional[str] = Field(None, description="Complemento do endereço")
    bairro: Optional[str] = Field(None, description="Nome do bairro")
    localidade: Optional[str] = Field(None, description="Cidade ou município")
    uf: Optional[str] = Field(None, description="Unidade federativa (estado)")
    ibge: Optional[str] = Field(None, description="Código IBGE do município")
    gia: Optional[str] = Field(None, description="Código GIA (apenas SP)")
    ddd: Optional[str] = Field(None, description="Código DDD da região")
    siafi: Optional[str] = Field(None, description="Código SIAFI do município")
    fonte: str
