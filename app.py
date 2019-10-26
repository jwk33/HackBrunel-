import sys
from flask import Flask,render_template,request
import requests
from google_maps import directions_map

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/directions")
def map_screen():
    destination = [request.args['destination']]
    print(destination + 'this one')
    url = directions_map(destination)
    print(url)
    return render_template('map_screen.html',url=url)
