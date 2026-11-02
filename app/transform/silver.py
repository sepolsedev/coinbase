class SilverTransformer:
    def transformar(self, dados):
        daily = dados["daily"]

        campos = {
            "data": "time",
            "temp_max": "temperature_2m_max",
            "temp_min": "temperature_2m_min",
            "sens_max": "apparent_temperature_max",
            "sens_min": "apparent_temperature_min",
            "vento_max": "wind_speed_10m_max",
            "nascer": "sunrise",
            "por_sol": "sunset",
            "luz_dia": "daylight_duration",
            "luz_sol": "sunshine_duration",
            "uv_max": "uv_index_max",
        }

        quantidade = len(daily["time"])
        registros = []

        for i in range(quantidade):
            registro = {
                destino: daily[origem][i]
                for destino, origem in campos.items()
            }

            registro["latitude"] = dados["latitude"]
            registro["longitude"] = dados["longitude"]
            registro["timezone"] = dados["timezone"]
            registros.append(registro)

        return registros
