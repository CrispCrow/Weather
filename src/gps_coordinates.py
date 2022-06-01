import geocoder

from .models.models import Coordinates


def get_coordinates() -> Coordinates:
    ip = geocoder.ip('me')
    location = ip.latlng

    return Coordinates(latitude=location[0],
                       longitude=location[1])
