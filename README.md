# 🌦️ ETL Weather Airflow

Este proyecto implementa un pipeline **ETL (Extract, Transform, Load)** automatizado y contenerizado utilizando **Apache Airflow** y **Docker**. Su objetivo principal es la ingesta continua de datos meteorológicos desde la API de [Open-Meteo](https://open-meteo.com/), su procesamiento y posterior almacenamiento en una base de datos **PostgreSQL** (Neon DB).

## 🚀 Características

*   **Extracción (Extract)**: Obtiene datos climáticos en tiempo real (temperatura, humedad, precipitación, viento, etc.) para coordenadas geográficas específicas.
*   **Transformación (Transform)**: Limpia, estructura y valida los datos recibidos utilizando **Pydantic**, asegurando la calidad de la información.
*   **Carga (Load)**: Inserta los datos procesados en una base de datos PostgreSQL utilizando **SQLModel** (ORM).
*   **Orquestación**: Utiliza **Apache Airflow** para programar y monitorear la ejecución diaria del flujo de trabajo.
*   **Infraestructura como Código**: Todo el entorno se despliega fácilmente mediante **Docker Compose**.

## 🛠️ Tecnologías

*   **Lenguaje**: Python 3.11+
*   **Orquestador**: Apache Airflow 2.9.0
*   **Contenedores**: Docker & Docker Compose
*   **Base de Datos**: PostgreSQL (Neon DB)
*   **Librerías Clave**:
    *   `sqlmodel`: Para el modelado y gestión de la base de datos.
    *   `pydantic`: Para la validación de esquemas de datos.
    *   `httpx`: Para realizar peticiones HTTP asíncronas a la API.

## 📂 Estructura del Proyecto

```
AirFlow-docker/
├── dags/                   # DAGs de Airflow (Punto de entrada)
│   └── dag_etl_weather.py
├── etl_weather/            # Módulo principal del proyecto
│   ├── db/                 # Configuración de conexión a BD
│   ├── ETL/                # Lógica del proceso (Extract, Transform, Load)
│   ├── model/              # Modelos de base de datos (Tablas)
│   ├── schemas/            # Esquemas de datos (Pydantic)
│   └── main.py             # Definición del DAG
├── docker-compose.yaml     # Configuración de servicios Docker
└── requirements.txt        # Dependencias del proyecto
```

## ⚙️ Instalación y Uso

### Prerrequisitos
*   Docker Desktop instalado y corriendo.
*   Una instancia de PostgreSQL (o una cuenta en Neon DB).

### Pasos para desplegar

1.  **Clonar el repositorio**:
    ```bash
    git clone <url-del-repositorio>
    cd AirFlow-docker
    ```

2.  **Configurar Variables de Entorno**:
    Crea un archivo `.env` en la raíz del proyecto con la siguiente variable:
    ```env
    NEON_DB=postgresql://usuario:password@host:port/nombre_db
    AIRFLOW_UID=50000
    ```

3.  **Iniciar Airflow**:
    Ejecuta el siguiente comando para levantar los contenedores:
    ```bash
    docker-compose up -d
    ```

4.  **Acceder a la Interfaz**:
    *   Abre tu navegador en [http://localhost:8080](http://localhost:8080).
    *   **Usuario**: `airflow`
    *   **Contraseña**: `airflow`

5.  **Activar el DAG**:
    Busca el DAG llamado `dag_etl_weather` y actívalo. Se ejecutará automáticamente una vez al día (`@daily`).

