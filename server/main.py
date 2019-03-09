from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
from geopy.geocoders import Nominatim
import requests
import json
import os

template_dir = "../client/templates"
static_dir = "../client/static"
app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)

@app.route('/', methods = ['GET', 'POST'])
def homepage():
    return render_template('home.html')

@app.route('/calculate')
def hotnessCalculator():
    location = geolocator.geocode("201 Mullica Hill Rd Glassboro")
    lat = location.latitude
    long = location.longitude
    return str(lat) + str(long)


@app.route('/test', methods = ['GET'])
def test():
    r = requests.get('https://eonet.sci.gsfc.nasa.gov/api/v2.1/events?days=20')
    return json.dumps(r.json())

if __name__ == '__main__':
    app.run()
