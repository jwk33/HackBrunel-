import requests
import json
from GPS import get_coords
waypoints = [(52.201156,0.114311),(52.201925, 0.115470)]
def directions(destinationCoordinates,waypoints):
    waypoints_list = []
    separator = '%7C'
    for i in waypoints:
        waypoints_list.append(str(i[0])+'%2C'+str(i[1]))
    print(waypoints_list)
    apiKey = "key=AIzaSyDYZzLkcTStJFATSjN2ZHotAucE2Z4q8Yc"
    #originCoordinates = get_coords()
    originCoordinates = [52.200591,0.113023]
    origin = "origin=" + str(originCoordinates[0]) + ',' + str(originCoordinates[1])
    destination = "destination=" + str(destinationCoordinates[0]) + ',' + str(destinationCoordinates[1])
    waypoints = 'waypoints='+  separator.join(waypoints_list)
    print(waypoints)
    url = "https://maps.googleapis.com/maps/api/directions/json?" + origin + '&' + destination + '&' + waypoints + '&'  + apiKey 
    print(url)

    try:
        getRequest = requests.get(url)
        data = getRequest.json()
        listRoute = data["routes"][0]["legs"]
        print(listRoute)
    except:
        print("Exception occured")
    
    #def coord_from_city():
    #    print("Hello World")

def directions_map(destinationCoordinates):
    
    apiKey = "key=AIzaSyDYZzLkcTStJFATSjN2ZHotAucE2Z4q8Yc"
    originCoordinates = get_coords()
    origin = "origin=" + str(originCoordinates[0]) + ',' + str(originCoordinates[1])
    destination = "destination=" + str(destinationCoordinates[0]) + ',' + str(destinationCoordinates[1])
    url = "https://www.google.com/maps/embed/v1/directions?" + origin + '&' + destination + '&'  + apiKey 
    return url

def directions_place(place):
    apiKey = "key=AIzaSyDYZzLkcTStJFATSjN2ZHotAucE2Z4q8Yc"    
    fields_place = 'fields=geometry/location'
    try:
        input = 'input='+ place
        inputType = 'inputtype=textquery'
        place_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?" + input + '&'  + inputType + '&' + fields_place +'&'  + apiKey 
        place_data = requests.get(place_url).json()
        destinationCoordinates = [place_data["candidates"][0]["geometry"]["location"]["lat"],place_data["candidates"][0]["geometry"]["location"]["lng"]]
        print(destinationCoordinates)
    except:
        print('Error')
    url_embed = directions_map(destinationCoordinates)
    return url_embed

if __name__ == "__main__":
    #directions([52.202333, 0.117272],waypoints)
    directions_place('The Shard')
    
