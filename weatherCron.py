import requests
import json

def get_lat_lon(zip_code):
    url = f"https://nominatim.openstreetmap.org/search?postalcode={zip_code}&format=json"
    headers = {
        "User-Agent": "weather_app"
    }
    response = requests.get(url, headers=headers)
    location_data = response.json()
    if location_data:
        return float(location_data[0]['lat']), float(location_data[0]['lon'])
    else:
        raise Exception("dude im Unable to retrieve location data for the given zip code.")

def get_weather_data(lat, lon):
    url = f"https://api.weather.gov/points/{lat},{lon}/forecast"
    headers = {
        "User-Agent": "weather_app",
        "Accept": "application/json"
    }
    response = requests.get(url, headers=headers)
    return response.json()

def save_weather_data_to_file(weather_data):
    with open("weather.log", "w") as f:
        json.dump(weather_data, f, indent=4)

if __name__ == "__main__":
    zip_code = input("Enter your zip code dude: ")
    try:
        lat, lon = get_lat_lon(zip_code)
        weather_data = get_weather_data(lat, lon)
        save_weather_data_to_file(weather_data)
        print("Weather data saved to weather.log, duderino")
    except Exception as e:
        print(f"Error: {e}")
