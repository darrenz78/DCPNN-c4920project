import json
from pymongo import MongoClient
# import requests
from flask import Flask
from flask import request
from flask_restplus import Resource, Api
from flask_restplus import fields
from flask_restplus import inputs
from flask_restplus import reqparse
import re
import random

# Helper Functions
app = Flask(__name__)
api = Api(app)

# Setup parser
parser = reqparse.RequestParser()
parser.add_argument('energy', type=int)

# chest/arm + leg + 
# GET http://127.0.0.1:5000/exercises?energy=LOW where LOW is a constant LOW=3 and HIGH=6

@api.route('/exercises')
class AllCollections(Resource):
    @api.expect(parser)
    def get(self):

        # Obtain energy entry
        args = parser.parse_args()
        energy = args['energy']

        # Connect to mongodb mlab
        mongo_port = 27107
        db_name = 'comp4920'
        collection_name = 'exercises'
        mongo_host = "mongodb://admin:admin123@ds331558.mlab.com:31558/comp4920"
        client = MongoClient(host=mongo_host, port=mongo_port)
        db = client[db_name]
        exercises = db[collection_name]

        # Obtain collection
        collection = db.exercises.find()

        output_list = []

        # Abort if collection not found
        if not collection:
            api.abort(404, "There are no collections in the database")

        # For testing, print out all records
        for record in collection:
            # print(record)
            exercise_id = record['id']
            exercise_name = record['exercise']
            description = record['description']
            muscle = record['muscle']
            photo = record['photo']
            output_dict = {
                "id": exercise_id,
                "exercise": exercise_name,
                "description": description,
                "photo": photo,
                "muscle": muscle,
                "compound": "false"
            }
            output_list.append(output_dict)
        # print(output_list)

        if energy:
            random.shuffle(output_list)
            return output_list[:energy], 200
        else:
            return output_list, 200


# Method used by developers only. Exercises will not be generated by the user
# def post(self)

if __name__ == '__main__':
    app.run(port=5001, debug=True)