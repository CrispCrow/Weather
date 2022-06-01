from typing import NamedTuple, Union, Annotated
from enum import Enum

Seconds = Annotated[int, 'Seconds']
Celsius = Annotated[int, 'Celsius']
MeterPerSecond = Annotated[float, 'MeterPerSecond']


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


class WeatherTypes(Enum):
    Thunderstorm = 'Thunderstorm'
    Drizzle = 'Drizzle'
    Rain = 'Rain'
    Snow = 'Snow'
    Mist = 'Mist'
    Smoke = 'Smoke'
    Haze = 'Haze'
    Dust = 'Dust'
    Fog = 'Fog'
    Sand = 'Sand'
    Ash = 'Ash'
    Squall = 'Squall'
    Tornado = 'Tornado'
    Clear = 'Clear'
    Clouds = 'Clouds'


class Weather(NamedTuple):
    sunrise: Union[Seconds, str]
    sunset: Union[Seconds, str]
    temperature: Celsius
    wind_speed: MeterPerSecond
    weather: WeatherTypes
