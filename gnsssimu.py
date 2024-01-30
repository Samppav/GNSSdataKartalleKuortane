
import json
import requests
import time
import geopy.distance

FILENAME = "position.txt"
total_distance = 0
with open(FILENAME, "r") as file:
    ekarivi = file.readline()
    ekalat = ekarivi.split("lat=")[1].split(",")[0]
    ekalon = ekarivi.split("lon=")[1].split(",")[0]
    coords_2 = (ekalat, ekalon)
    for line in file:
        lat = float(line.split("lat=")[1].split(",")[0])
        lon = float(line.split("lon=")[1].split(",")[0])
        obj = [lat, lon]
        print(lat, lon)
        coords_1 = (lat, lon)
        total_distance += geopy.distance.geodesic(coords_1, coords_2).km
        print(total_distance)
        response = requests.post("http://localhost:5000/uusimittaus", json = obj)
        print(response.ok, response.json())
        time.sleep(0.1)
        coords_2 = (lat, lon)