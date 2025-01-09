import requests
import json

def get_temperature(location_name, latitude: float, longitude:float):
    # API call
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m&temperature_unit=fahrenheit"

    # GET request to API
    try:
        response = requests.get(url)
        if response.status_code == 200:
            temperature = response.json()
            return temperature
        else:
            print("Error: ", response.status_code)
            return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

response = get_temperature(40.7188,-111.8505)
print(response)
temperature = response['current']['temperature_2m']
print(temperature)