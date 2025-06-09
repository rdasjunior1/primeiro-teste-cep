from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
    api_token: str

    class Config:
        env_file = ".env"

settings = Settings()
print("🔍 Token dentro do dependencies.py:", settings.api_token)
