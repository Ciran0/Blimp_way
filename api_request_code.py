import requests
import json
import math

API_KEY = 'e623da52f797357b9c0e8cdc625d8eb3'

def get_coordinates\
                (city_name):
    url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        i = response.json()
        return [i[0]["lat"], i[0]["lon"]]
    else:
        print(f"Failed to fetch data. Error code: {response.status_code}")
        return None


def fetch_weather_data(latitude, longitude):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        i = response.json()
        return i["wind"]
    else:
        print(f"Failed to fetch data. Error code: {response.status_code}")
        return None

def get_points_between_coordinates(depart, arrive, n):
    if n < 2:
        raise ValueError("n must be at least 2.")

    lats = [depart[0]]
    lons = [depart[1]]

    depart_wdata = fetch_weather_data(depart[0],depart[1])

    speed = [depart_wdata["speed"]]
    deg = [depart_wdata["deg"]]

    for i in range(1, n):
        f = float(i) / float(n)
        lat = depart[0] + (arrive[0] - depart[0]) * f
        lon = depart[1] + (arrive[1] - depart[1]) * f
        lats.append(lat)
        lons.append(lon)

        step_wdata = fetch_weather_data(lat,lon)
        speed.append(step_wdata["speed"])
        deg.append(step_wdata["deg"])
    
    lats.append(arrive[0])
    lons.append(arrive[1])

    arrive_wdata = fetch_weather_data(arrive[0],arrive[1])

    speed.append(arrive_wdata["speed"])
    deg.append(arrive_wdata["deg"])

    return json.dumps(list(zip(lats, lons, speed, deg)))

# Example usage:

#depart = get_coordinates("paris")  # Example departure coordinates (New York City)
#arrive = get_coordinates("milan")  # Example arrival coordinates (Los Angeles)
#n = 5  # Example number of points

#points = get_points_between_coordinates(depart, arrive, n)
#print(points)


#wdata = fetch_weather_data(depart[0],depart[1])

#print(wdata["speed"])
#print(wdata["deg"])
