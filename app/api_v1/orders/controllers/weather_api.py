import requests as req
from core.config import settings


def get_weather_by_cords(latitude:str, longitude:str):
    url_yandex = f'https://api.weather.yandex.ru/v2/informers/?lat={latitude}&lon={longitude}&[lang=ru_RU]'
    yandex_req = req.get(url_yandex, headers={'X-Yandex-API-Key': '771c47c8-130d-4d35-b352-696502b21ff1'}).json()

    return yandex_req["fact"]
    