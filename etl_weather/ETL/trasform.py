from datetime import datetime
from etl_weather.schemas.weather import WeatherData

def parser_data(data: dict) -> WeatherData:
    """Extrae el último registro horario de Open-Meteo"""

    hourly = data["hourly"] # Apuntamos al objeto con los daros relevantes
    i = -1  # último índice disponible
    
    # Metemos los datos en el modelo
    data = WeatherData(
        time=hourly["time"][i],
        temp_2m=hourly["temperature_2m"][i],
        apparent_temp=hourly["apparent_temperature"][i],
        relative_humidity_2m=hourly["relative_humidity_2m"][i],
        precipitation=hourly["precipitation"][i],
        weathercode=hourly["weathercode"][i],
        cloudcover=hourly["cloudcover"][i],
        wind_speed_10m=hourly["wind_speed_10m"][i],
        latitude=data["latitude"],
        longitude=data["longitude"],
        extraction_time= datetime.utcnow().isoformat()
    )
    
    return data
    