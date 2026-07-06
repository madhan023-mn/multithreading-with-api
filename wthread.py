import os
from dotenv import load_dotenv
import threading
import requests
import time
load_dotenv()

Cities=["Hyderabad",
        "Mumbai",
        "Pune",
        "Delhi",
        "Chennai"
        ]

responses=[]
def get_weather_info(city):
    print(f"Fecting the weather for {city}\n")
    url = f"http://api.weatherapi.com/v1/current.json?key={os.getenv('APIKEY')}&q={city}"
    response=requests.get(url)
    data=response.json()
    responses.append({
    "City": data["location"]["name"],
    "Country": data["location"]["country"],
    "Temperature (°C)": data["current"]["temp_c"],
    "Humidity (%)": data["current"]["humidity"]
})
    

threads=[]

start=time.time()

for city in Cities:
    thread=threading.Thread(target=get_weather_info,args=(city,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end=time.time()

print(f"\nTotal time {end-start:.2f} seconds\n ")
print("-"*60)
for data in responses:
    print(data)
    #print("-"*100)

