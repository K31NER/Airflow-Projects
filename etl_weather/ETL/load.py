from etl_weather.model.weather import WeatherTabla
from etl_weather.schemas.weather import WeatherData
from etl_weather.db.config_db import get_connection,startup

def load_data(data: dict):
    try:
        # Validación + mapping
        new_data = WeatherTabla.parse_obj(data)

        with get_connection() as db:
            db.add(new_data)
            db.commit()

    except ValueError as e:
        print(f"Error de validación de datos: {e}")
        raise

    except Exception as e:
        print(f"Error al insertar datos en la base de datos: {e}")
        raise