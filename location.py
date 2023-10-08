import requests

class Location:

    def __init__(self) -> None:
        self._api_key = 'AIzaSyDMfqJfekH6iVvgpEXEiU3Mbo3q4LZTv5I'

    def get_all_location(self, list_address:list) -> tuple:

        url = f'https://maps.googleapis.com/maps/api/geocode/json?address={list_address}&key={self._api_key}'

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            if data['status'] == 'OK':
                location = data['results'][0]['geometry']['location']
                latitud = location['lat']
                longitud = location['lng']

                return latitud, longitud
            else:
                print('No se pudo encontrar la ubicación.')
                return 'error', 'No se pudo encontrar la ubicación.'
        else:
            print('Error al hacer la solicitud a la API Geocoding.')
            return 'error', 'Error al hacer la solicitud a la API Geocoding.'



if __name__ == '__main__':
    location = Location()
    direccion = 'DE LOS ARQUEROS 17917, 27800, CHIHUAHUA, MX'

    latitude, longitude = location.get_all_location(direccion)

    print(f'Latitude: {latitude}\nLongitude: {longitude}')