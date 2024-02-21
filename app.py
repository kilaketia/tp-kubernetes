import os
import json
import sys
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import mysql.connector

APP_PORT = os.environ.get('APP_PORT')

mydb = mysql.connector.connect(
  host="mariadb-service.killian-page.svc.cluster.local",
  user="root",
  password="admin"
)

cursor = mydb.cursor()

cursor.execute("show databases;")
for db in cursor:
    if db == "configs":
        dbCreated = True
    else: 
        dbCreated = False
    
if dbCreated: 
    cursor.execute("USE configs")
    cursor.execute("SELECT value FROM keysta WHERE keyname='message'")
    result = cursor.fetchone()
    if result:
        MESSAGE = result
        return result  # Return the value of 'message'
    else:
        return None  # If 'message' entry doesn't exist
else: 
    cursor.execute("CREATE DATABASE IF NOT EXISTS configs")
    cursor.execute("USE configs")
    cursor.execute('''CREATE TABLE IF NOT EXISTS keysta
                     (keyname VARCHAR(255) PRIMARY KEY, value VARCHAR(255))''')
    cursor.execute('INSERT INTO keysta VALUES ("message","DB works")')
    mydb.commit()
    MESSAGE = "Just been initialized"

cursor.close()
mydb.close()

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