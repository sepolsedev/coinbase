import json
from datetime import datetime, timezone
from pathlib import Path


class BronzeStorage:
    def __init__(self,path="data/bronze"):
        self.path = Path(path)
        self.path.mkdir(parents=True, exist_ok=True)

    def salvar(self, dados):
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        arquivo = self.path / f"clima_{timestamp}.json"

        with arquivo.open("w",encoding="utf-8") as f :
            json.dump(dados, f, ensure_ascii=False,indent=4)
            return arquivo



        