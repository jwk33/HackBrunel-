import geocoder
import requests

def get_city():
    g = geocoder.ipinfo('me')
    return g

def get_coords():
    print(get_city().latlng)
    return get_city().latlng

def convert_to_coords(place):
    p = geocoder.google(place)
    print(p)
    return p

def get_location():
    r = requests.get('https://api.ipdata.co?api-key=test').json()
    ltlng = (r["latitude"],r["longitude"])
    return ltlng

if __name__ == "__main__":
    #get_city()
    #get_coords()
    #convert_to_coords("Uxbridge, London")
    get_location()