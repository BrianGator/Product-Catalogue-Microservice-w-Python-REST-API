import unittest
from service import app
from service.common import status
from tests.factories import ProductFactory

class TestProductRoutes(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_get_product_list(self):
        response = self.client.get("/products")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
