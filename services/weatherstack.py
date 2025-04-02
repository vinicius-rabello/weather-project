import requests
import os
from base import WeatherService
from datetime import date, timedelta

class WeatherStackService(WeatherService):
    
    def __init__(self):
        self.API_KEY = os.environ.get('WEATHERSTACK_API_KEY')
        self.BASE_URL = f'https://api.weatherstack.com/current?access_key={self.API_KEY}'


    def get_forecast(self, location):
        lat, lon = location
        res = requests.get(self.BASE_URL, params={
            'query': lat + ', '+ lon,
            'forecast_days': 1})
        data = res.json()
        return data