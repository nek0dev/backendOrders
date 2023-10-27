from pydantic_settings import BaseSettings
import dotenv
import os

dotenv.load_dotenv()

class Setting(BaseSettings):
    db_url: str = os.getenv("DB_URL")
    db_echo: bool = True
    weather_token: str = os.getenv("WEATHER_API_KEY")
    jwt_secret:str = os.getenv("JWT_SECRET")
    jwt_algorithm:str = os.getenv("JWT_ALGORITHM")
    hash_salt:str = os.getenv("HASH_SALT")

settings = Setting()
