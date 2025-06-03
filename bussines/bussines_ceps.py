import asyncio
from client.client_ceps import get_cep_api_1, get_cep_api_2
from schemas.cep_response import CepResponse
from fastapi import HTTPException

def buscar_cep(cep: str) -> CepResponse:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    dados_cep = loop.run_until_complete(pegar_mais_rapido(cep))
    loop.close()

    if not dados_cep or "erro" in dados_cep:
        raise HTTPException(status_code=404, detail="CEP não encontrado")

    return CepResponse(
        cep=dados_cep.get("cep", ""),
        logradouro=dados_cep.get("logradouro", ""),
        complemento=dados_cep.get("complemento", ""),
        bairro=dados_cep.get("bairro", ""),
        localidade=dados_cep.get("localidade", ""),
        uf=dados_cep.get("uf", ""),
        ibge=dados_cep.get("ibge", ""),
        gia=dados_cep.get("gia", ""),       
        ddd=dados_cep.get("ddd", ""),         
        siafi=dados_cep.get("siafi", "")     
)

async def pegar_mais_rapido(cep: str):
    task1 = asyncio.create_task(get_cep_api_1(cep))
    task2 = asyncio.create_task(get_cep_api_2(cep))

    done, pending = await asyncio.wait(
        [task1, task2],
        return_when=asyncio.FIRST_COMPLETED
    )

    for task in pending:
        task.cancel()

    return list(done)[0].result()  