from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
import requests
import json
import os

template_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
template_dir = os.path.join(template_dir, 'client')
template_dir = os.path.join(template_dir, 'templates')

static_dir = os.path.dirname(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
static_dir = os.path.join(static_dir, 'client')
static_dir = os.path.join(static_dir, 'static')
app = Flask(__name__, static_folder=static_dir, template_folder=template_dir)

@app.route('/', methods = ['GET'])
def test():
    r = requests.get('https://eonet.sci.gsfc.nasa.gov/api/v2.1/events?days=20')
    return json.dumps(r.json())

if __name__ == '__main__':
    app.run()
