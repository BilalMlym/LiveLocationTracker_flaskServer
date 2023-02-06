

from flask import Flask, request, jsonify
import requests, json, random
from flask_cors import CORS, cross_origin




app = Flask(__name__)
CORS(app, supports_credentials=True)

@cross_origin(supports_credentials=True)
def login():
  return jsonify({'success': 'ok'})

if __name__ == "__main__":
  app.run(port=5000, debug=True)
@app.route('/AAA', methods = ["GET"] )
def AAA():
  return'<h1>hello<h1>'



@app.route('/home', methods = ["POST"] )
def home():
    
    data = request.get_json()
    latitude = data['latitude']
    longitude = data['longitude']
    location = latitude,longitude
  
    
    print(latitude, longitude)
    return(location)
