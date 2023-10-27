from .weather_api import get_weather_by_cords


def inspect_weather(latitude:str, longitude: str) -> bool:
    weather = get_weather_by_cords(latitude=latitude, longitude=longitude)
    temp_cond = int(weather['temp']) < -1 or int(weather['temp']) > 40
    wind_cond = int(weather['wind']) > 25

    if temp_cond and wind_cond: return False
    
    return True