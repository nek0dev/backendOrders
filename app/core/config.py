from pydantic_settings import BaseSettings
import dotenv
import os
dotenv.load_dotenv()

class Setting(BaseSettings):
    db_url: str = os.getenv("DB_URL")
    db_echo: bool = True


settings = Setting()
