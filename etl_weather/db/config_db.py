import os
from dotenv import load_dotenv
from contextlib import contextmanager
from etl_weather.model.weather import WeatherTabla
from sqlmodel import Session,create_engine,SQLModel

load_dotenv()
URI = os.getenv("NEON_DB")
engine = create_engine(url=URI)

@contextmanager
def get_connection():
    with Session(engine) as session:
        yield session
        
def startup():
    """ Inicializa la base de datos"""
    
    print("Creando tablas...")    
    SQLModel.metadata.create_all(engine)
    print("Tabla creadas con exito")