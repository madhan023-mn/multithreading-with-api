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

responses=[]
def get_weather_info(city):
    print(f"Fecting the weather for {city}\n")
    url = f"http://api.weatherapi.com/v1/current.json?key={os.getenv('APIKEY')}&q={city}"
    response=requests.get(url)
    responses.append(response.json())
    print(f"{city} : {response.status_code}")


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
    print("-"*100)



    

