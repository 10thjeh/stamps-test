# . Display the weather forecast for Jakarta for the next 5 days

# Please use the API provided at http://openweathermap.org.
# Display the output as the weather forecast for Jakarta for the next 5 days.
# Only show one temperature per day.
# This task does not require a paid account.
import requests
import os
from dotenv import load_dotenv
from time import strftime, localtime
load_dotenv()

BASE_URL = os.getenv("BASE_OPENWEATHER_URL_API")
API_KEY = os.getenv("OPENWEATHER_API_KEY")

JAKARTA_LAT = str(-6.200000)
JAKARTA_LON = str(106.816666)

def generateApiURL(param: str) -> str:
    return BASE_URL + param + "&appid=" + API_KEY

def weather():
    url = generateApiURL("forecast?units=metric&lat=" + JAKARTA_LAT +  "&lon=" + JAKARTA_LON)

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather_list = data['list']
        skips = int(len(weather_list)/5)
        days = weather_list[::skips]
        for day in days:
            print(strftime('%a, %d %b %Y', localtime(day['dt'])), ":", day['main']['temp'], '°C')
    else:
        print("Failed!")
    
    return

weather()