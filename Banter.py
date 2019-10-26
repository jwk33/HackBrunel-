import json as json

with open("derulo.json") as fp:
    settings = json.loads(fp.read())

import struct as struct

from network import network

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(settings["username"], settings["password"])

while not station.isconnected():
    pass

networks = station.scan()

data = {
    "considerIp": False,
    "wifiAccessPoints": []
}


entry = {
    "macAddress": "%02x:%02x:%02x:%02x:%02x:%02x" % struct.unpack("BBBBBB", wifi[1]),
    "signalStrength": wifi[3],
    "channel": wifi[2]
}
data["wifiAccessPoints"].append(entry)

import requests as requests

headers = {"Content-Type": "application/json"}
url = "https://www.googleapis.com/geolocation/v1/geolocate?key=" + settings["api_key"]

response = requests.post(url, headers=headers, data=json.dumps(data))
location = json.loads(response.content)["location"]