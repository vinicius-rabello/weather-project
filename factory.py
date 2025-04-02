from services.weatherapi import WeatherAPIService
from services.openweathermap import OpenWeatherMapService

class WeatherServiceFactory:
    SERVICES = {
        'weatherapi': WeatherAPIService,
        'openweathermap': OpenWeatherMapService
    }

    @staticmethod
    def get_service(service_name):
        service_class = WeatherServiceFactory.SERVICES.get(service_name.lower())
        if not service_class:
            raise ValueError(f"Unknown weather service: {service_name}")
        return service_class()