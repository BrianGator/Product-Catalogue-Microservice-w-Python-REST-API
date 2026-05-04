import unittest
from service import app
from service.common import status

class TestSecurity(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_input_validation_enforcement(self):
        """Ensure bad types are rejected with 400 Bad Request"""
        payload = {
            "name": "Hacker Product",
            "price": "not-a-number",
            "category": "TOOLS"
        }
        response = self.client.post("/products", json=payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
