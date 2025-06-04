import asyncio
from client.client_ceps import fetch_cep_viacep, fetch_cep_brasilapi
from schemas.cep_response import CepResponse
from fastapi import HTTPException

async def buscar_cep(cep: str) -> CepResponse:
    if not cep.isdigit() or len(cep) != 8:
        raise HTTPException(status_code=400, detail="CEP inválido") 

    dados_cep = await pegar_mais_rapido(cep)

    if not dados_cep or "erro" in dados_cep:
        raise HTTPException(status_code=404, detail="CEP não encontrado")

    return CepResponse(**dados_cep)

def parse_viacep(data: dict) -> dict:
    return {
        "cep": data.get("cep", ""),
        "logradouro": data.get("logradouro", ""),
        "complemento": data.get("complemento", ""),
        "bairro": data.get("bairro", ""),
        "localidade": data.get("localidade", ""),
        "uf": data.get("uf", ""),
        "ibge": data.get("ibge", ""),
        "gia": data.get("gia", ""),
        "ddd": data.get("ddd", ""),
        "siafi": data.get("siafi", ""),
        "fonte": "viacep"
    }

def parse_brasilapi(data: dict) -> dict:
    return {
        "cep": data.get("cep", ""),
        "logradouro": data.get("street", ""),
        "complemento": "",
        "bairro": data.get("neighborhood", ""),
        "localidade": data.get("city", ""),
        "uf": data.get("state", ""),
        "ibge": "",
        "gia": "",
        "ddd": "",
        "siafi": "",
        "fonte": "brasilapi"
    }

async def pegar_mais_rapido(cep: str) -> dict:
    async def api_1(cep_local):
        data = await fetch_cep_viacep(cep_local)
        return parse_viacep(data)

    async def api_2(cep_local):
        data = await fetch_cep_brasilapi(cep_local)
        return parse_brasilapi(data)


    apis = [api_1, api_2]

    tasks = [asyncio.create_task(api(cep)) for api in apis]

    done, pending = await asyncio.wait(

        tasks, return_when=asyncio.FIRST_COMPLETED

        )

    for task in pending:
        task.cancel()

    return list(done)[0].result()
