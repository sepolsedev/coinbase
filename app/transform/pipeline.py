import logging

from app.extract.open_meteo import OpenMeteoCliente
from app.load.bronze import BronzeStorage
from app.load.database import Database
from app.transform.silver import SilverTransformer
from app.transform.gold import GoldTransformer


class Pipeline:
    def __init__(self, latitude, longitude, database_url):
        self.latitude = latitude
        self.longitude = longitude

        self.api = OpenMeteoCliente(latitude, longitude)
        self.bronze = BronzeStorage()
        self.silver = SilverTransformer()
        self.gold = GoldTransformer()
        self.database = Database(database_url)

    def executar(self):
        try:
            logging.info("Iniciando pipeline.")

            dados = self.api.buscar_previsao()
            logging.info("Dados extraídos com sucesso.")

            self.bronze.salvar(dados)
            self.database.inserir_bronze(
                self.latitude,
                self.longitude,
                dados,
            )
            logging.info("Dados salvos na Bronze.")

            registros_silver = self.silver.transformar(dados)
            self.database.inserir_silver(registros_silver)
            logging.info("Dados carregados na Silver com sucesso.")

            registros_gold = self.gold.transformar(registros_silver)
            self.database.inserir_gold(registros_gold)
            logging.info("Dados carregados na Gold com sucesso.")

            logging.info("Pipeline finalizada com sucesso.")

        except Exception:
            logging.exception("Erro durante a execução da pipeline.")
            raise

        finally:
            self.database.fechar()
