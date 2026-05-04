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

    def test_user_agent_compatibility(self):
        """Verify various User-Agents are handled correctly"""
        headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X)"}
        response = self.client.get("/", headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_accept_language_compatibility(self):
        """Verify internationalization headers don't break the app"""
        headers = {"Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7"}
        response = self.client.get("/products", headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_cross_origin_request_headers(self):
        """Verify CORS related headers are processed"""
        headers = {"Origin": "http://example.com"}
        response = self.client.options("/products", headers=headers)
        self.assertIn(response.status_code, [200, 204, 404, 405])

    def test_date_header_consistency(self):
        """Verify the server provides a valid Date header"""
        response = self.client.get("/")
        self.assertIn("Date", response.headers)

    def test_content_length_header(self):
        """Verify Content-Length is provided for API responses"""
        response = self.client.get("/products")
        self.assertIn("Content-Length", response.headers)

    def test_numeric_precision_compatibility(self):
        """Verify that high precision decimals are handled consistently"""
        payload = {"name": "Precision Test", "description": "Desc", "price": "99.9999", "available": True, "category": "TOOLS"}
        response = self.client.post("/products", json=payload)
        self.assertEqual(response.status_code, 201)
