import json

import requests

weather_map_api_key = 'a006c9c582dde2994f646473fb0efcc5'
toronto = (43.6532, -79.3832)
etobicoke = (43.69161, -79.54647)
asofa = (5.65840, -0.27726)

def weather_out(loc):
    lat = loc[0]
    lon = loc[1]
    api_key = weather_map_api_key
    print(lat, '  ', lon)
    url = 'http://api.openweathermap.org/data/2.5/weather?lat=%s&lon=%s&APPID=%s&units=metric/' % (lat, lon, api_key)
    response = requests.get(url)
    print(url)
    if response.ok:
        data = json.loads(response.text)
        print(data)
    else:
        print('Backend weather service not available')


weather_out(etobicoke)
weather_out(toronto)
weather_out(asofa)
