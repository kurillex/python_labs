import requests
import json
from translate import Translator

city = "Saint Petersburg"


def get_weather_api():
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': "5ff5ff55442ec19bd90f9334041f2cd5",
        'units': 'metric',
    }
    response = requests.get(url, params=params)

    analysis(response)
    get_useful_weather_info(response)


def get_useful_weather_info(response):
    data = response.json()
    weather_description = translate_text(data['weather'][0]['description'])
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']

    print(f"\nПогода: {weather_description}")
    print(f"Температуа: {temperature}°C")
    print(f"Влажность: {humidity}%")
    print(f"Давление: {pressure} кПа")





