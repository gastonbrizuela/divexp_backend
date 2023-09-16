#config.py 
import os
from flask_sqlalchemy import SQLAlchemy

#crea un objeto de la base de datos
db = SQLAlchemy()

# definir la clase config que contiene las variables de configuracion

class Config:
    # obtener el nombre de la base de datos desde una variable de entorno o usar uno por uno por defecto
    DATABASE_NAME = os.environ.get("DATABASE_NAME") or "logindatabase"
    
    DATABASE_USER = os.environ.get("DATABASE_USER") or 'postgres'
    
    DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")  or '150687'
    
    DATABASE_HOST = os.environ.get("DATABASE_HOST") or "localhost"
    
    DATABASE_PORT = os.environ.get("DATABASE_PORT") or "5432"
    #consturi la url de la base de datos usando los valores anteriores·
    SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:150687@localhost:5432/Logindatabase"
    # desactivar el seguimiento de modificaciones para evitar el consumo innecesario de memoria
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.environ.get("SECRET_KEY") or "secret"


