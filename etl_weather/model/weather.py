from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

class WeatherTabla(SQLModel, table=True):
    __tablename__ = "weather"
    id: Optional[int] = Field(default=None,primary_key=True)
    time: datetime
    temp_2m : float
    apparent_temp: float
    relative_humidity_2m: int
    precipitation: float
    weathercode: int
    cloudcover: int
    wind_speed_10m: float
    latitude: float
    longitude: float
    extraction_time: datetime
    
