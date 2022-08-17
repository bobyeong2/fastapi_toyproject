import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME:str = "Job Board"
    PROJECT_VERSION: str = "1.0.0"

    MYSQL_USER : str = os.getenv("DB_USER")
    MYSQL_PASSWORD = os.getenv("DB_PASSWD")
    MYSQL_HOST : str = os.getenv("DB_HOST","localhost")
    MYSQL_PORT : str = os.getenv("DB_PORT",3306) # default postgres port is 5432
    MYSQL_DB : str = os.getenv("DB_NAME","test")
    DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset=utf8"

settings = Settings()