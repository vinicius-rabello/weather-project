from abc import ABC, abstractmethod

class WeatherService(ABC):
    """Abstract base class for weather services."""
    
    @abstractmethod
    def get_forecast(self, location):
        """Fetch the weather forecast for a given location."""
        pass