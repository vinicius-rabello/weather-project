import requests
import os
from base import WeatherService
from datetime import date, timedelta

class OpenWeatherMapService(WeatherService):
    
    def __init__(self):
        self.API_KEY = os.environ.get('OPENWEATHERMAP_API_KEY')
        self.BASE_URL = f'http://api.openweathermap.org/data/2.5/forecast?'

    def get_forecast(self, location):
        lat, lon = location
        url = self.BASE_URL + f'lat={lat}&lon={lon}&appid={self.API_KEY}'
        res = requests.get(url)
        data = res.json()
        days = data['list']
        day = days[0]
        weather = day['weather']
        rain_indicator = f'{weather[0]['main']} {weather[0]['description']}'
        return rain_indicator