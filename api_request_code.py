import requests
import json

API_KEY = 'e623da52f797357b9c0e8cdc625d8eb3'
lat = 1
lon = 1

def get_coordinates(city_name):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q=London&limit=1&appid={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        i = response.json()
        return [i[0]["lat"],i[0]["lon"]]
    else:
        print(f"Failed to fetch data. Error code: {response.status_code}")
        return None

def fetch_weather_data(latitude,longitude):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        i = response.json()
        return i["wind"]
    else:
        print(f"Failed to fetch data. Error code: {response.status_code}")
        return None
    
