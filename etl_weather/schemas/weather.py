from datetime import datetime
from pydantic import BaseModel

class WeatherData(BaseModel):
    time: datetime
    temp_2m: float
    apparent_temp: float
    relative_humidity_2m: int
    precipitation: float
    weathercode: int
    cloudcover: int
    wind_speed_10m: float
    latitude: float
    longitude: float
    extraction_time: datetime