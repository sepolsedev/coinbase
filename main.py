import logging

from app.transform.pipeline import Pipeline
from config.settings import LATITUDE, LONGITUDE, DATABASE_URL


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)


if __name__ == "__main__":
    pipeline = Pipeline(
        latitude=LATITUDE,
        longitude=LONGITUDE,
        database_url=DATABASE_URL,
    )
    pipeline.executar()
