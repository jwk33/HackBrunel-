import sys
from flask import Flask,render_template,request
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/directions")
def map_screen():
    print('hello world')
    destination = request.args['destination']
    url = "https://maps.googleapis.com/maps/api/directions/json?origin=51.5489,-0.4821&destination=" + destination + '&key=AIzaSyDYZzLkcTStJFATSjN2ZHotAucE2Z4q8Yc'
    data = requests.get(url)
    return render_template('map_screen.html')
