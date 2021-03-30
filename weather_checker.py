import requests


class WeatherChecker:

    def __init__(self):
        self.apiKey = "88tUwZYdPHaWQiIh5erRHObnawYcrmh6FvE3BjAg"
        self.weather_url = "https://www.metaweather.com/"
        self.post_urt = "https://api.postcodes.io/postcodes/"
        self.postcode = ""
        self.latitude = ""
        self.longitude = ""
        self.woeid = ""

    def set_lat_long(self, postcode):
        self.postcode = postcode
        json = requests.get(self.post_urt + postcode).json()
        try:
            self.latitude = json['result']['latitude']
            self.longitude = json['result']['longitude']
        except KeyError:
            raise Exception("Postcode invalid")

    def set_woeid(self, lat, long):
        querystring = f"api/location/search/?lattlong={lat},{long}"
        self.woeid = requests.get(self.weather_url + querystring).json()[0]['woeid']
        return self.woeid

    def get_weather(self, woeid):
        querystring = f"api/location/{woeid}/"
        get = requests.get(self.weather_url + querystring).json()["consolidated_weather"][0]
        return f"At {self.postcode}, the weather is {get['weather_state_name'].lower()} with a predicted temperature of {get['the_temp']} celsuis"

    def run_checker(self, postcode):
        weather.set_lat_long(postcode)
        weather.set_woeid(weather.latitude, weather.longitude)
        return weather.get_weather(weather.woeid)


if __name__ == "__main__":
    weather = WeatherChecker()

    while True:
        usr_input = input("Do you want to check the weather? y or n: ")
        if usr_input.lower() == "n":
            break

        usr_input = input("Please enter the postcode you want to check: ").strip()
        try:
            print(weather.run_checker(usr_input))
        except Exception as errmsg:
            print(errmsg)


