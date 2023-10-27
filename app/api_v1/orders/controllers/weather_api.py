import json
import requests as req
from core.config import settings
import asyncio


def get_weather_by_cords(latitude:str, longitude:str):
    url_yandex = f'https://api.weather.yandex.ru/v2/forecast/?lat={latitude}&lon={longitude}&[lang=ru_RU]'
    yandex_req = req.get(url_yandex, headers={'X-Yandex-API-Key': settings.weather_token}).json()
    return yandex_req["fact"]
    