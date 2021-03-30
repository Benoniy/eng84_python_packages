import requests


class WeatherChecker:

    def __init__(self):
        self.apiKey = "88tUwZYdPHaWQiIh5erRHObnawYcrmh6FvE3BjAg"
        self.weather_url = "https://www.metaweather.com/"
        self.post_urt = "https://api.postcodes.io/postcodes/"
        self.latitude = ""
        self.longitude = ""
        self.woeid = ""

    def set_lat_long(self, postcode):
        json = requests.get(self.post_urt + postcode).json()
        self.latitude = json['result']['latitude']
        self.longitude = json['result']['longitude']

    def set_woeid(self, lat, long):
        querystring = f"api/location/search/?lattlong={lat},{long}"
        self.woeid = requests.get(self.weather_url + querystring).json()[0]['woeid']
        return self.woeid



if __name__ == "__main__":
    weather = WeatherChecker()
    weather.set_lat_long("co152aa")
    print(weather.set_woeid(weather.latitude, weather.longitude))
