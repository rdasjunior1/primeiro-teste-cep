import httpx 

async def fetch_cep_viacep(cep: str) -> dict:
    url = f"https://viacep.com.br/ws/{cep}/json/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, timeout=5)
        if response.status_code != 200:
            return {"erro": True}
        return response.json()
    
async def fetch_cep_brasilapi(cep: str) -> dict:
    url = f"https://brasilapi.com.br/api/cep/v1/{cep}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, timeout=5)
        if response.status_code !=200:
            return {"erro": True}
        return response.json()