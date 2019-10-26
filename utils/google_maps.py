import requests
import json
from GPS import get_coords

def directions(destinationCoordinates):
    originCoordinates = get_coords()
    origin = "origin=" + str(originCoordinates[0]) + ',' + str(originCoordinates[1])
    destination = "destination=" + str(destinationCoordinates[0]) + ',' + str(destinationCoordinates[1])

    apiKey = "key=AIzaSyDYZzLkcTStJFATSjN2ZHotAucE2Z4q8Yc"
    url = "https://maps.googleapis.com/maps/api/directions/json?" + origin + '&' + destination + '&' + apiKey

    try:
        getRequest = requests.get(url)
        data = getRequest.json()
        listRoute = data["routes"][0]["legs"]
        print(listRoute)
    except:
        print("Exception occured")

if __name__ == "__main__":
    directions([52.200677, 0.113066])
