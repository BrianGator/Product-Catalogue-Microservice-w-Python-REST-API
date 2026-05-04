import unittest
from service import app

class TestCompatibility(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_json_utf8_compatibility(self):
        """Ensure the API handles and returns valid UTF-8 JSON"""
        payload = {"name": "Müniç Item", "description": "Special Characters Check", "price": "10.00", "available": True, "category": "TOOLS"}
        response = self.client.post("/products", json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        data = response.get_json()
        self.assertEqual(data["name"], "Müniç Item")
