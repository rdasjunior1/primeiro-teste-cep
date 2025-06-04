import os
from typing import Annotated
from fastapi import Header, HTTPException
from dotenv import load_dotenv
from settings import settings

load_dotenv()

def get_token(authorization: Annotated[str, Header()] = "") ->str:
    if not authorization.startswith("Bearer"):
        raise HTTPException(status_code=401, detail="Token invalido")
    
    token = authorization.removeprefix("Bearer").strip()
    if token != settings.api_token:
        raise HTTPException(status_code=401, detail="Token invalido")
    return token