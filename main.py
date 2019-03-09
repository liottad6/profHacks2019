from flask import Flask
import requests
import json

r = requests.get('https://eonet.sci.gsfc.nasa.gov/api/v2.1/events?days=20')
print(json.dumps(r.json()))
