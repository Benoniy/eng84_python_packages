# API for postcode IO
import requests


url = "http://api.postcodes.io/postcodes/"
postcode = "e147le"


url_arg = url + postcode
print(url_arg)
response = requests.get(url_arg)
print(response.status_code)

print(response.content)

print(response.headers)

print(response.cookies)

print(response.is_redirect)

response_dict = response.json()
print(response_dict)

result_dict = response_dict["result"]

for key, val in result_dict.items():
    print(key, val)



