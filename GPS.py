import geocoder

def get_location():
    g = geocoder.ipinfo('me')
    return g

if __name__ == "__main__":
    get_location()