import json
import psycopg

class Database:
    def __init__(self, connection_string):
        self.connection = psycopg.connect(connection_string)

    def inserir_bronze(self, latitude, longitude, dados):
        with self.connection.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO bronze.previsoes_raw
                  (latitude, longitude, dados)
                VALUES (%s, %s, %s)
                """,
                (
                    latitude,
                    longitude,
                    json.dumps(dados, ensure_ascii=False)
                )
            )
        self.connection.commit()

    def inserir_silver(self, registros):
        with self.connection.cursor() as cursor:
            for r in registros:
                cursor.execute(
                    """
                    INSERT INTO silver.previsoes_diarias(
                        latitude, longitude, data, timezone,
                        temp_max, temp_min,
                        sens_max, sens_min,
                        vento_max, nascer, por_sol,
                        luz_dia, luz_sol, uv_max
                    )
                    VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (latitude, longitude, data)
                    DO UPDATE SET
                        timezone = EXCLUDED.timezone,
                        temp_max = EXCLUDED.temp_max,
                        temp_min = EXCLUDED.temp_min,
                        sens_max = EXCLUDED.sens_max,
                        sens_min = EXCLUDED.sens_min,
                        vento_max = EXCLUDED.vento_max,
                        nascer = EXCLUDED.nascer,
                        por_sol = EXCLUDED.por_sol,
                        luz_dia = EXCLUDED.luz_dia,
                        luz_sol = EXCLUDED.luz_sol,
                        uv_max = EXCLUDED.uv_max,
                        atualizado_em = CURRENT_TIMESTAMP
                    """,
                    (
                        r["latitude"], r["longitude"], r["data"],
                        r["timezone"], r["temp_max"], r["temp_min"],
                        r["sens_max"], r["sens_min"], r["vento_max"],
                        r["nascer"], r["por_sol"], r["luz_dia"],
                        r["luz_sol"], r["uv_max"]
                    )
                )
        self.connection.commit()

    def inserir_gold(self, registros):
        with self.connection.cursor() as cursor:
            for r in registros:
                cursor.execute(
                    """
                    INSERT INTO gold.indicadores_clima(
                    latitude, longitude, data, temperatura_media, amplitude_termica,
                    sensacao_media, vento_max, uv_max)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT(latitude, longitude, data)
                    DO UPDATE SET
                        temperatura_media = EXCLUDED.temperatura_media,
                        amplitude_termica = EXCLUDED.amplitude_termica,
                        sensacao_media = EXCLUDED.sensacao_media,
                        vento_max = EXCLUDED.vento_max,
                        uv_max = EXCLUDED.uv_max,
                        atualizado_em = CURRENT_TIMESTAMP
                    """,
                    (
                     r["latitude"], r["longitude"], r["data"], r["temperatura_media"],
                     r["amplitude_termica"], r["sensacao_media"], r["vento_max"], r["uv_max"],
                    ),
                )
        self.connection.commit()

    def fechar(self):
        self.connection.close()
