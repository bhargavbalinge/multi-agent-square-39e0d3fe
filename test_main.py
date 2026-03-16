import unittest
import json
from main import app

class TestSquareCalculator(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_calculate_success(self):
        response = self.app.post('/calculate', 
                                 data=json.dumps({'number': 5}), 
                                 content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['result'], 25)

    def test_calculate_invalid_input(self):
        response = self.app.post('/calculate', 
                                 data=json.dumps({'number': 'abc'}), 
                                 content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)

    def test_calculate_no_input(self):
        response = self.app.post('/calculate', 
                                 data=json.dumps({}), 
                                 content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()