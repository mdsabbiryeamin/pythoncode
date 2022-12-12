import requests
city_name='Dhaka'
API_KEY='dda94182ee1218053ebd78f87d01bf95'
weather_url= f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
requs=requests.get(weather_url)
jsonData =requs.json()

city =jsonData.get('name')
country =jsonData.get('sys').get('country')
tem =jsonData.get('main').get('temp')
print(f'weather City Name: {city}, weather country Name: {country}, weather tem : {tem}')
