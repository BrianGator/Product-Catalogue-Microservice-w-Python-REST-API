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
