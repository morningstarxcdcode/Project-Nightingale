import unittest
import json
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.app import app

class TestFlaskAPI(unittest.TestCase):
    
    def setUp(self):
        """Set up test client"""
        self.app = app.test_client()
        self.app.testing = True
    
    def test_home_endpoint(self):
        """Test the home endpoint"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn("Welcome to Project Nightingale API", data['message'])
    
    def test_health_endpoint(self):
        """Test the health endpoint"""
        response = self.app.get('/api/health')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'healthy')
    
    def test_data_endpoint_success(self):
        """Test the data endpoint with valid data"""
        test_data = {'data': 'Test input for AI model'}
        response = self.app.post('/api/data', 
                                json=test_data,
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertIn('ai_result', data)
    
    def test_data_endpoint_missing_data(self):
        """Test the data endpoint with missing data field"""
        test_data = {'wrong_field': 'value'}
        response = self.app.post('/api/data', 
                                json=test_data,
                                content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)
    
    def test_predict_endpoint_success(self):
        """Test the predict endpoint with valid input"""
        test_data = {'input': 'Prediction test data'}
        response = self.app.post('/api/predict', 
                                json=test_data,
                                content_type='application/json')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertIn('prediction', data)
    
    def test_predict_endpoint_missing_input(self):
        """Test the predict endpoint with missing input field"""
        test_data = {'wrong_field': 'value'}
        response = self.app.post('/api/predict', 
                                json=test_data,
                                content_type='application/json')
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.data)
        self.assertIn('error', data)

if __name__ == "__main__":
    unittest.main()