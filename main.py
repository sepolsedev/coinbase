from config.settings import(
    LATITUDE,LONGITUDE,DATABASE_URL,
)

if __name__ == "__main__":
    pipeline = Pipeline(
        latitude=LATITUDE,
        longitude=LONGITUDE,
        database_url=DATABASE_URL,
    )
    pipeline.executar()