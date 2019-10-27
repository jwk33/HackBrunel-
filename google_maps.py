import requests
import json
from GPS import get_coords, convert_to_coords
from PIL import Image, ImageDraw, ImageFilter
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

def directions_places(place):
    apiKey = "key=AIzaSyDYZzLkcTStJFATSjN2ZHotAucE2Z4q8Yc"
    originCoordinates = get_coords()
    origin = "origin=" + str(originCoordinates[0]) + ',' + str(originCoordinates[1])
    destination = "destination=" + place
    fields_place = 'fields=geometry/location'
    try:
        input = 'input=name'
        inputType = 'inputtype=textquery'
        place_url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?" + destination + '&'  + input + '&'  + inputType + '&' + fields_place +'&'  + apiKey 
        place_data = requests.get(place_url).json()
        print(place_data)
        
    except:
        print('Error')

def static_map_image(place):
    url = "https://maps.googleapis.com/maps/api/staticmap?"
    api_key = "AIzaSyDYZzLkcTStJFATSjN2ZHotAucE2Z4q8Yc"
    center = place
    zoom = 14
    r = requests.get(url + "center=" + center + "&zoom=" + str(zoom) + "&format=jpeg&size=400x400&maptype=road&style=feature:landscape.natural%7Celement:labels.text.fill%7Cvisibility:on%7Ccolor:0xffffff&key=" + api_key)
    f = open('tester.jpg', 'wb') 
    f.write(r.content)
    f.close()

def image_editor():
    im_rgb = Image.open('test.png').convert("RGBA")
    im_rgb.putalpha(100)
    background = Image.open("mapboi.jpg").convert("RGBA")
    foreground = im_rgb
    background.paste(foreground, (0, 0), foreground)
    background.show()
    background.save('maper.png', format="png")

if __name__ == "__main__":
    directions([52.202333, 0.117272],waypoints)
    directions_places('Queens\' College')
    static_map_image("London")
    image_editor()
    
