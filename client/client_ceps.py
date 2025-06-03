import httpx

async def get_cep_api_1(cep: str) -> dict:
    url = f"https://viacep.com.br/ws/{cep}/json/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, timeout=5)
        return response.json()

async def get_cep_api_2(cep: str) -> dict:
    # Simulando outra API (por enquanto usa ViaCEP também)
    url = f"https://viacep.com.br/ws/{cep}/json/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, timeout=5)
        return response.json()
    