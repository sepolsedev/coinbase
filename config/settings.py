import os
from dotenv import load_dotenv

load_dotenv()

LATITUDE = float(os.getenv("LATITUDE", "-16.68"))
LONGITUDE = float(os.getenv("LONGITUDE", "-46.25"))
TIMEZONE = os.getenv("TIMEZONE", "auto")

DB_NAME = os.getenv("DB_NAME", "clima")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

DATABASE_URL = (
    f"dbname={DB_NAME} "
    f"user={DB_USER} "
    f"password={DB_PASSWORD} "
    f"host={DB_HOST} "
    f"port={DB_PORT}"
)
