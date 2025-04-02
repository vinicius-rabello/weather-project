from factory import WeatherServiceFactory
import pandas as pd
import os
from dotenv import load_dotenv

service_names = [
    'weatherapi',
    'openweathermap'
]

load_dotenv()

LAT = os.environ.get('LAT')
LON = os.environ.get('LON')

data = []
for service_name in service_names:
    row = []
    service = WeatherServiceFactory.get_service(service_name)
    forecast = service.get_forecast([LAT, LON])
    row.extend([service_name, forecast])
    data.append(row)

df = pd.DataFrame(data=data, columns=['service', 'will_it_rain'])
df.to_excel('pred.xlsx', index=False)