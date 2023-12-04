
import json
import requests
import time
 
FILENAME = "position.txt"
 
with open(FILENAME, "r") as file:
    for line in file:

        lat = float(line.split("lat=")[1].split(",")[0])
        lon = float(line.split("lon=")[1].split(",")[0])
        obj = [lat, lon]
        print(lat, lon)
        response = requests.post("http://localhost:5000/uusimittaus", json = obj)
        print(response.ok, response.json())
        time.sleep(0.1)