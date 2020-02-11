import os
from env import GOOGLE_API_KEY

GOOGLE_APIS = {
    'geolocation': 'https://www.googleapis.com/geolocation/v1/geolocate?key=%s' % GOOGLE_API_KEY,
    'geocoding': 'https://maps.googleapis.com/maps/api/geocode/json?'
}


if __name__ == "__main__":
    print(GOOGLE_APIS)
    