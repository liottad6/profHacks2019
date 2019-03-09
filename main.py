from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/', methods = ['GET'])
def test():
    r = requests.get('https://eonet.sci.gsfc.nasa.gov/api/v2.1/events?days=20')
    return json.dumps(r.json())



if __name__ == '__main__':
    app.run()
