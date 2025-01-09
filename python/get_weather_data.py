import requests
import json

def get_temperature_data(location_name, latitude: float, longitude:float):
    # API call
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m&temperature_unit=fahrenheit"

    # GET request to API
    try:
        response = requests.get(url)
        if response.status_code == 200:
            temperature = response.json()['current']['temperature_2m']
        else:
            print("Error: ", response.status_code)
            return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
    return [location_name, latitude, longitude, temperature]

response = get_temperature_data("Salt Lake City",40.4000,-111.8505)
#temperature = response['current']['temperature_2m']
#print(temperature)