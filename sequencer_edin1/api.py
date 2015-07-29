from flask import Flask, request
from flask_restful import Resource, Api, reqparse

from pymongo import MongoClient

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('key', type=str)
parser.add_argument('value', type=int)

mongo = MongoClient()
db = mongo.sequencer
keys_values = db.keys_values

resources = {
    'value_url': '/value',
}

class Home(Resource):
    def get(self):
        return resources

class ValueUrl(Resource):
    def get(self, key):
        result_db = keys_values.find_one({"key": key})
        if result_db is None:
            keys_values.insert_one({"key": key, "value": 0})
            value_db = 0
        else:
            value_db = result_db["value"]
        keys_values.update({"key": key}, {"$inc": {"value": 1}})
        return {'value': value_db}

    def post(self, key):
        args = parser.parse_args()
        result_db = keys_values.find_one({"key": key})
        if result_db is None:
            keys_values.insert_one({"key": key, "value": args["value"]})
        else:
            keys_values.update({"key": key}, {"value": args["value"]})
        return {'value': args["value"]}

api.add_resource(Home, '/')
api.add_resource(ValueUrl, '%s/<string:key>'%resources['value_url'])

if __name__ == '__main__':
    app.run(debug=True)