#!/usr/bin/env python3

from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route("/biotools")
def home():
    datafh = open('biotools.json', 'r')
    data = datafh.read()
    datafh.close()
    resp = Response(data, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Allow'] = 'GET, HEAD, OPTIONS'
    return resp
	
def run():
  sys.exit(app.run())

if __name__ == "__main__":
    app.run()