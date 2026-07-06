import os
import requests
from dotenv import load_dotenv
import threading
import time

load_dotenv()
Cities=["Hyderabad",
        "Mumbai",
        "Pune",
        "Delhi",
        "Chennai"
        ]

def get_weather_info(city):
    print(f"Fecting the weather for {city}\n")
    url = f"http://api.weatherapi.com/v1/current.json?key={os.getenv('APIKEY')}&q={city}"
    try:
        response=requests.get(url)
        data=response.json()
        return data
    except Exception  as e:
        print("error",e)
start=time.time()
for city in Cities:
    data=get_weather_info(city)
    if data:
        print(data)
        print("-"*100)
end=time.time()
print(f"\nTotal time {end-start:.2f} seconds ")
    

