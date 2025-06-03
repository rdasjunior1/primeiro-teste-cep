import httpx

async def get_cep_api_1(cep: str) -> dict:
    # ViaCEP
    url = f"https://viacep.com.br/ws/{cep}/json/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, timeout=5)
        if response.status_code != 200:
            return {"erro": True}
        data = response.json()
        if "erro" in data:
            return {"erro": True}
        data["fonte"] = "viacep"
        return data

async def get_cep_api_2(cep: str) -> dict:
    url = f"https://brasilapi.com.br/api/cep/v1/{cep}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, timeout=5)
        data = response.json()

        if response.status_code != 200:
            return {"erro": True}
        return {
            "cep": data.get("cep", ""),              # mudou code -> cep
            "logradouro": data.get("street", ""),   # mudou address -> street
            "bairro": data.get("neighborhood", ""),# mudou district -> neighborhood
            "localidade": data.get("city", ""),
            "uf": data.get("state", ""),
            "complemento": "",
            "ibge": "",
            "gia": "",
            "ddd": "",
            "siafi": "",
            "fonte": "brasilapi"
        }