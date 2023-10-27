from .weather_api import get_weather_by_cords

def good_weather_state(state: str) -> bool:
    validate_word = {"clear", "partly-cloudy", "overcast", "cloudy",
                "drizzle",}
    
    if state in validate_word: return True

    return False


def inspect_weather(latitude:str, longitude: str) -> bool:
    weather = get_weather_by_cords(latitude=latitude, longitude=longitude)

    temp_cond = int(weather['temp']) < -1 or int(weather['temp']) > 40
    wind_cond = int(weather['wind_speed']) > 25

    if temp_cond or wind_cond or not good_weather_state(weather['condition']): return False
    
    return True