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

    def test_database_uri_presence(self):
        """Verify DB URI is configured"""
        self.assertIn("SQLALCHEMY_DATABASE_URI", app.config)

    def test_404_error_handler(self):
        """Verify system handles unknown routes with 404"""
        client = app.test_client()
        response = client.get("/non-existent-route")
        self.assertEqual(response.status_code, 404)

    def test_405_error_handler(self):
        """Verify system handles wrong methods with 405"""
        client = app.test_client()
        response = client.put("/products") # Missing ID should 405 or 404
        self.assertIn(response.status_code, [404, 405])

    def test_app_debug_mode(self):
        """Verify debug mode is disabled for safety"""
        self.assertFalse(app.debug)

    def test_logger_initialization(self):
        """Verify the app logger is active"""
        self.assertTrue(app.logger.isEnabledFor(20)) # INFO level

    def test_template_folder_path(self):
        """Verify template folder configuration"""
        self.assertTrue(os.path.exists(app.template_folder))
