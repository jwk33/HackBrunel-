import geocoder

def get_city():
    g = geocoder.ipinfo('me')
    return g

def get_coords():
    print(get_city().latlng)
    return get_city().latlng

if __name__ == "__main__":
    get_city()
    get_coords()