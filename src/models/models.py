from typing import NamedTuple, Union, Annotated, Final
from enum import Enum

Seconds = Annotated[int, 'Seconds']
Celsius = Annotated[int, 'Celsius']
MeterPerSecond = Annotated[float, 'MeterPerSecond']


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


class WeatherTypes(Enum):
    THUNDERSTORM: Final = 'Thunderstorm'
    DRIZZLE: Final = 'Drizzle'
    RAIN: Final = 'Rain'
    SNOW: Final = 'Snow'
    MIST: Final = 'Mist'
    SMOKE: Final = 'Smoke'
    HAZE: Final = 'Haze'
    DUST: Final = 'Dust'
    FOG: Final = 'Fog'
    SAND: Final = 'Sand'
    AAH: Final = 'Ash'
    SQUALL: Final = 'Squall'
    TORNADO: Final = 'Tornado'
    CLEAR: Final = 'Clear'
    CLOUDS: Final = 'Clouds'


class Weather(NamedTuple):
    sunrise: Union[Seconds, str]
    sunset: Union[Seconds, str]
    temperature: Celsius
    wind_speed: MeterPerSecond
    weather: WeatherTypes
