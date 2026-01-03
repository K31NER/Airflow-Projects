import httpx

# Definimos als coordenadas de colombia
LAT, LON = 4.71,-74.07

def get_weather(lat: float = LAT, lon: float = LON) -> dict:
    """ Consulta el clima usando la api de open meteo
    
    Parametros:
    - lat: latitud
    - lon: longitud 
    
    Return:
    - json: Json con los datos meteorologicos
    """
    
    # Definimos la URL para consumir la API de Open-Meteo
    URL = (
    f"https://api.open-meteo.com/v1/forecast?"      # Endpoint base
    f"latitude={lat}&longitude={lon}"               # Coordenadas geográficas
    f"&current_weather=true"                        # Clima actual
    f"&hourly="                                     
    f"temperature_2m,"                              # Temperatura del aire a 2 metros (°C)
    f"apparent_temperature,"                        # Sensación térmica percibida (°C)
    f"relative_humidity_2m,"                        # Humedad relativa a 2 metros (%)
    f"precipitation,"                               # Precipitación acumulada (mm)
    f"weathercode,"                                 # Código numérico del estado del clima
    f"cloudcover,"                                  # Porcentaje de nubosidad (%)
    f"wind_speed_10m"                               # Velocidad del viento a 10 metros (km/h)
    )    
    try:
        # Realizamos la peticon
        respone = httpx.get(URL,timeout=15)
        
        respone.raise_for_status()
        
    except httpx.TimeoutException as e:
        raise RuntimeError("Timeout al consultar Open-Meteo") from e

    except httpx.HTTPStatusError as e:
        raise RuntimeError(
            f"Error HTTP {e.response.status_code} desde Open-Meteo"
        ) from e
    # Devolvemos el json
    return respone.json()

if __name__ == "__main__":
    print(get_weather())
