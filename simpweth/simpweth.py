import requests


class Weather:
    """Creates a Weather object getting apikey as input
    and either a city name or latitude and longitude coordinates values.

    Package use example:

    * Get a valid apikey at https://openweather.org (activating your apikey may take some time)

    * Create a Weather object using city name:
    >>> weather1 = Weather(city='Kek', apikey='720ebffe1ed99acb48bbf6c3851c4780')
    # This apikey is not guaranteed to work

    * Using latitude and longitude:
    >>> weather2 = Weather(lat=48.1149173, lon=21.8778149, apikey='720ebffe1ed99acb48bbf6c3851c4780')
    # If city name is provided along with lon and lat arguments, city name will be ignored.

    * Get complete weather data for the next 12 hours:
    >>> weather1.next_12h()

    * Simplified data for next 12 hours
    >>> weather1.next_12h_simplified()

    Sample url to get weather condition icons:
    http://openweathermap.org/img/wn/10d@2x.png

    """
    def __init__(self, lat=None, lon=None, city=None, apikey=None):
        if not apikey:
            raise TypeError("provide apikey along with a city or lat AND lon arguments")
        elif lat and lon:
            self.data = self._lat_lon_provided(lat, lon, apikey)
        elif city:
            self.data = self._city_provided(city, apikey)
        else:
            raise TypeError("provide either a city or lat AND lon arguments")
        if not self.data:
            raise ValueError("invalid city name")
        elif self.data['cod'] != '200':
            raise ValueError(self.data['message'])

    @staticmethod
    def _lat_lon_provided(lat, lon, apikey):
        url = f"https://api.openweathermap.org/data/2.5/forecast" \
              f"?lat={lat}&lon={lon}&appid={apikey}&units=metric"
        return requests.get(url).json()

    def _city_provided(self, city, apikey):
        url = f"http://api.openweathermap.org/geo/1.0/direct" \
              f"?q={city}&limit=5&appid={apikey}"
        response = requests.get(url).json()
        # if city name is invalid API returns an empty response with status '200'
        if not response:
            return
        # if invalid apikey passed along with valid city name response appears as a dict with status code and a message
        if isinstance(response, dict):
            return response
        # passing valid arguments gives us a list of dictionaries
        lat, lon = response[0]['lat'], response[0]['lon']
        return self._lat_lon_provided(lat, lon, apikey)

    def next_12h(self):
        """Returns 3-hour data for the next 12 hours as a list of dictionaries.
        """
        return self.data['list'][:4]

    def next_12h_simplified(self):
        """Returns date, temperature, and sky condition every 3 hours
           for the next 12 hours as a tuple of tuples
        """
        data = []
        for weather in self.next_12h():
            data.append((weather['dt_txt'], weather['main']['temp'], weather['weather'][0]['description'],
                         weather['weather'][0]['icon']))
        return tuple(data)
