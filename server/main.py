from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
from geopy.geocoders import Nominatim
from array import *

import requests
import json
import os

template_dir = "../client/templates"
static_dir = "../client/static"
geolocator = Nominatim(user_agent="HotSingleWildfiresInYourArea")
app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)

def searchHotSingles():
    rdata = requests.get('https://eonet.sci.gsfc.nasa.gov/api/v2.1/events?days=5')
    data = rdata.json()
    allEvents = []
    pairCoords = []
    for events in data['events']:
        for geometries in events['geometries']:
            for coords in geometries['coordinates']:
                allEvents.append(coords)
                print (coords)
    x = 0
    while (x < len(allEvents)):
        y = 0
        pairCoords.insert(y, [allEvents[x],allEvents[x+1]])
        x += 2
        y += 1  
    print (pairCoords)
    
    with open('readthis.json', 'w') as f:
        z = 0
        while (z < len(pairCoords)):
            f.write("%s\n" % str(pairCoords[z]))
            z += 1

@app.route('/', methods = ['GET', 'POST'])
def homepage():
    searchHotSingles()
    return render_template('home.html')

@app.route('/calculate', methods = ['POST'])
def hotnessCalculator():
    location = request.form['location']
    loc = geolocator.geocode(location)
    lat = loc.latitude
    long = loc.longitude
    searchHotSingles()
    return str(lat) + str(long)
# for each of the elements in the

@app.route('/test', methods = ['GET'])
def test():
    r = requests.get('https://eonet.sci.gsfc.nasa.gov/api/v2.1/events?days=5')
    return json.dumps(r.json())

if __name__ == '__main__':
    app.run()
