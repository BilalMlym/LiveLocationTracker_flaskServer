

from flask import Flask, request, jsonify
import requests, json, random
from flask_cors import CORS, cross_origin
from random import choice



app = Flask(__name__)
CORS(app, supports_credentials=True)

@cross_origin(supports_credentials=True)
def login():
  return jsonify({'success': 'ok'})

if __name__ == "__main__":
  app.run(port=5000, debug=True)


@app.route('/home', methods = ["GET","POST"] )
def location():
    
    data = request.get_json()
    latitude = data['latitude']
    longitude = data['longitude']
    location = latitude,longitude
    print(location)
   

    return(data)
