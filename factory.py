from services.weatherapi import WeatherAPIService
from services.openweathermap import OpenWeatherMapService
from services.weatherstack import WeatherStackService
from services.tomorrow import TomorrowService

class WeatherServiceFactory:
    SERVICES = {
        'weatherapi': WeatherAPIService,
        'openweathermap': OpenWeatherMapService,
        'weatherstack': WeatherStackService,
        'tomorrow': TomorrowService
    }

    @staticmethod
    def get_service(service_name):
        service_class = WeatherServiceFactory.SERVICES.get(service_name.lower())
        if not service_class:
            raise ValueError(f"Unknown weather service: {service_name}")
        return service_class()