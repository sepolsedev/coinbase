import requests

from config.settings import TIMEZONE

class OpenMeteoCliente:
    BASE_URL ="https://api.open-meteo.com/v1/forecast"

    def __init__(self, latitude, longitude, timezone=TIMEZONE):
        self.latitude = latitude
        self.longitude = longitude
        self.timezone = timezone
        

    def buscar_previsao(self):
        params = {
            "latitude":self.latitude,
            "longitude":self.longitude,
            "daily":",".join([
                "temperature_2m_max",
                "temperature_2m_min",
                "apparent_temperature_max",
                "apparent_temperature_min",
                "wind_speed_10m_max",
                "sunrise",
                "sunset",
                "daylight_duration",
                "sunshine_duration",
                "uv_index_max",
            ]),
            "timezone":self.timezone,
        }
        response = requests.get(
            self.BASE_URL,
            params=params,
            timeout=30,
        )

        response.raise_for_status()
        return response.json()