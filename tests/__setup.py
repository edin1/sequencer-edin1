import unittest

from pymongo import MongoClient

from sequencer_edin1.api import app
import sequencer_edin1.api

mongo = MongoClient()
db = mongo.sequencer
db.drop_collection("test_keys_values")
keys_values = db.test_keys_values
sequencer_edin1.api.keys_values = keys_values

test_app = app.test_client()

class TestCase(unittest.TestCase):
    def _cleanup(self):
        keys_values.drop()

    def setUp(self):
        # global keys_values
        # keys_values = db.test_keys_values
        pass

    def tearDown(self):
        keys_values.drop()
        pass
