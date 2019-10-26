import requests

def directions(originCoordinates,destinationCoordinates):
    origin = "origin=" + str(originCoordinates[0]) + ',' + str(originCoordinates[1])
    destination = "destination=" + str(destinationCoordinates[0]) + ',' + str(destinationCoordinates[1])

    apiKey = "key=AIzaSyDYZzLkcTStJFATSjN2ZHotAucE2Z4q8Yc"
    url = "https://maps.googleapis.com/maps/api/directions/json?" + origin + '&' + destination + '&' + apiKey

    try:
        r = requests.get(url)
        print(r.json())
    except:
        print("Exception occured")

if __name__ == "__main__":
    directions([52.201407, 0.114321],[52.200677, 0.113066])
