import requests
import datetime

from .gps_coordinates import get_coordinates
from .models.models import Weather
from settings import config


def get_weather_info() -> Weather:
    coordinates = get_coordinates()

    response = requests.get(
        config['api_url_template'].format(
            lat=coordinates.latitude,
            lon=coordinates.longitude,
            units=config['api_config']['units'],
            lang=config['api_config']['language'],
            api_key=config['api_key'])
    ).json()

    return Weather(
        sunrise=parse_time(response['current']['sunrise']),
        sunset=parse_time(response['current']['sunset']),
        temperature=round(response['current']['temp']),
        wind_speed=round(response['current']['wind_speed']),
        weather=response['current']['weather'][0]['main']
    )


def parse_time(seconds: int) -> str:
    date = datetime.datetime.fromtimestamp(seconds)

    return date.strftime('%H:%M:%S')

