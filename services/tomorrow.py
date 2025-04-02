import requests
import os
from base import WeatherService
from datetime import date, timedelta

class TomorrowService(WeatherService):
    
    def __init__(self):
        self.api_key = os.environ.get('TOMORROW_API_KEY')
        self.BASE_URL = 'https://api.tomorrow.io/v4/weather/forecast'
        self.tomorrow = date.today() + timedelta(days=1)
        self.tomorrow_date = self.tomorrow.isoformat()

    def get_forecast(self, location):
        lat, lon = location
        res = requests.get(self.BASE_URL, params={
            'location': lat + ', '+ lon,
            'apikey': self.api_key})
        data = res.json()
        days = data['timelines']['daily']
        for day in days:
            if day['time'].split('T')[0] == self.tomorrow_date:
                return day['values']['precipitationProbabilityMax']
        return None