import requests
import os
from base import WeatherService
from datetime import date, timedelta

class WeatherAPIService(WeatherService):
    
    def __init__(self):
        self.api_key = os.environ.get('WEATHERAPI_API_KEY')
        self.BASE_URL = 'http://api.weatherapi.com/v1/forecast.json'

    def get_forecast(self, location):
        res = requests.get(self.BASE_URL, params={'key': self.api_key, 'q': location})
        data = res.json()
        day = data['forecast']['forecastday'][0]['day']
        rain_chance = day['daily_chance_of_rain']
        return rain_chance