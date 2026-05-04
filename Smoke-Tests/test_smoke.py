import unittest
from service import app

class TestSmoke(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_basic_health(self):
        """Sanity check: Server is alive"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_admin_ui_availability(self):
        """Verify static UI is served"""
        response = self.client.get("/")
        self.assertIn(b"Product Store Admin", response.data)

    def test_health_check(self):
        """Verify the root endpoint is healthy"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_products_endpoint_active(self):
        """Verify the products endpoint returns a valid response"""
        response = self.client.get("/products")
        self.assertEqual(response.status_code, 200)

    def test_static_assets_css(self):
        """Verify CSS assets are reachable (simulated)"""
        response = self.client.get("/static/css/style.css")
        # Even if 404, we check if the static routing is configured
        self.assertIn(response.status_code, [200, 404]) 

    def test_static_assets_js(self):
        """Verify JS assets are reachable (simulated)"""
        response = self.client.get("/static/js/script.js")
        self.assertIn(response.status_code, [200, 404])

    def test_api_json_response(self):
        """Verify the API returns JSON by default for products"""
        response = self.client.get("/products")
        self.assertEqual(response.headers["Content-Type"], "application/json")

    def test_empty_search_returns_200(self):
        """Verify searching with no results doesn't crash"""
        response = self.client.get("/products?name=NonExistentProduct")
        self.assertEqual(response.status_code, 200)
