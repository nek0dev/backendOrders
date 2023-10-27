from .weather_api import get_weather_by_cords

def good_weather_state(state: str) -> bool:
    validate_word = {
        "clear", "partly-cloudy", "overcast", "cloudy",
        "light-rain"
    }
    
    if state in validate_word: return True

    return False


def inspect_weather(latitude:str, longitude: str) -> bool:
    weather = get_weather_by_cords(latitude=latitude, longitude=longitude)

    temp_cond = int(weather['temp']) < -1 or int(weather['temp']) > 40
    wind_cond = int(weather['wind_speed']) > 25
    wind_gust = int(weather['wind_gust']) > 12

    if temp_cond or wind_cond or not good_weather_state(weather['condition']) or wind_gust: return False
    
    return True