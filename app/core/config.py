from pydantic_settings import BaseSettings
import dotenv
import os


class Setting(BaseSettings):
    db_url: str = "postgresql+asyncpg://postgres:postgres@localhost/postgres"
    db_echo: bool = True


settings = Setting()
