import colorama
from colorama import Fore
colorama.init()
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "your api" # your api key on the site openweather.org
CITY = input("city? ")

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celcius = temp_kelvin-273.15

feels_like_kelvin = response['main']['feels_like']
feels_like_celcius = feels_like_kelvin-273.15

humidity = response['main']['humidity']

wind_speed_ms = response['wind']['speed']
wind_speed_kmh = wind_speed_ms * 3.6

print(f"{Fore.YELLOW}Temperature in {CITY}: {Fore.RESET}{temp_celcius:.2f}°C\n{Fore.YELLOW}Feels like: {Fore.RESET}{feels_like_celcius:.2f}°C\n{Fore.LIGHTBLUE_EX}Wind speed: {Fore.RESET}{wind_speed_ms} m/s = {wind_speed_kmh} km/h\n{Fore.LIGHTBLUE_EX}Humidity in {CITY}: {Fore.RESET}{humidity}%")
input()
