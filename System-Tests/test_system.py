import unittest
import os
from service import app

class TestSystem(unittest.TestCase):
    def test_server_config(self):
        """Verify server configurations are loaded"""
        self.assertFalse(app.config["SQLALCHEMY_TRACK_MODIFICATIONS"])
        self.assertTrue(app.static_folder.endswith("static"))

    def test_middleware_rejection(self):
        """Internal System Check: Reject missing content type"""
        client = app.test_client()
        response = client.post("/products", data="bad data")
        self.assertEqual(response.status_code, 415)
