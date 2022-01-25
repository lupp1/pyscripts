# Weather API fetcher - gives data about weather

import requests
from time import sleep

API_KEY = 'cf5f02151129f98a991a9aeb56447550'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"


city = input('Enter a city name: ')
request_url = f'{BASE_URL}?appid={API_KEY}&q={city}'
request = requests.get(f'{request_url}')
data = request.json()

def response():
    if request.status_code == 200:  # HTTPs - OK response
        print(f'Temperature for {city.title()}\n',
    f'{round(data["main"]["temp"] - 273.15, 2)}ºC NOW\n', 
    f'{round(data["main"]["temp_min"] - 273.15, 2)}ºC MIN\n',
    f'{round(data["main"]["temp_max"] - 273.15, 2)}ºC MAX'
    )

    else:
        print('An error occurred.')

response()
sleep(10)