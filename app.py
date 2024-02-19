import os
import json
import sys
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

#MESSAGE = os.environ.get('MESSAGE')
with open('/volume/message.txt') as f:
    try:
        MESSAGE = f.readline()
    except:
        print("Lecture du fichier impossible !")
APP_PORT = os.environ.get('APP_PORT')

# creating the flask app
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False 
api = Api(app)

class get(Resource):
    def get(self):
        return {"message": MESSAGE}, 200

api.add_resource(get, "/")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        if sys.argv[1] == "debug":
            app.run(host='0.0.0.0', port=APP_PORT,debug=True)
    else:
        app.run(host='0.0.0.0', port=APP_PORT)
