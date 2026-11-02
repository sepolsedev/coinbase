class GoldTransformer:
    def transformar(self, registros):
        resultado = []

        for registro in registros:
            temp_media = (
                registro["temp_max"] + registro["temp_min"]
            ) / 2

            amplitude = (
                registro["temp_max"] - registro["temp_min"]
            )

            sens_media = (
                registro["sens_max"] + registro["sens_min"]
            ) / 2

            resultado.append({
                "latitude": registro["latitude"],
                "longitude": registro["longitude"],
                "data": registro["data"],
                "temperatura_media": round(temp_media, 2),
                "amplitude_termica": round(amplitude, 2),
                "sensacao_media": round(sens_media, 2),
                "vento_max": registro["vento_max"],
                "uv_max": registro["uv_max"],
            })

        return resultado
