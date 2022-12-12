import requests
import pprint
city_name='Dhaka'
API_KEY='dda94182ee1218053ebd78f87d01bf95'
weather_url= f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'
requs=requests.get(weather_url)
pprint.pprint(requs.json())
