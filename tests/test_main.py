import json

from .__setup import TestCase, test_app

from sequencer_edin1.api import resources

def json_load(req):
    return json.loads(req.data.decode('utf-8'))

class MainTest(TestCase):
    def test_home(self):
        req = test_app.get('/')
        data = json_load(req)
        self.assertEqual(data, resources)

    def test_value(self):
        req = test_app.get('/value')
        self.assertEqual(req.status_code, 404)

    def test_value_get_initialize(self):
        req = test_app.get('/value/test_value')
        data = json_load(req)
        self.assertEqual(data, {"value": 0})

    def test_value_get_increment(self):
        test_app.get('/value/test_value')
        req = test_app.get('/value/test_value')
        data = json_load(req)
        self.assertEqual(data, {"value": 1})

    def test_value_post(self):
        req = test_app.post('/value/test_value',
                            data={"key": "test_value", "value": 3})
        data = json_load(req)
        self.assertEqual(data, {"value": 3})
