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

    def test_create_product_success(self):
        """Verify product creation via API"""
        payload = {"name": "API Prod", "description": "Test", "price": "12.00", "available": True, "category": "TOOLS"}
        response = self.client.post("/products", json=payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_product_not_found(self):
        """Verify 404 for invalid ID"""
        response = self.client.get("/products/999999")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_product_api(self):
        """Verify PUT update works"""
        p = ProductFactory().create()
        payload = {"name": "Updated", "description": "Test", "price": "10.00", "available": True, "category": "TOOLS"}
        response = self.client.put(f"/products/{p.id}", json=payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.get_json()["name"], "Updated")

    def test_delete_product_api(self):
        """Verify DELETE removal"""
        p = ProductFactory().create()
        response = self.client.delete(f"/products/{p.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_search_by_category_api(self):
        """Verify filtering by category"""
        ProductFactory(category=Category.TOOLS).create()
        response = self.client.get("/products?category=TOOLS")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.get_json()) >= 1)

    def test_invalid_content_type(self):
        """Verify 415 for non-json POST"""
        response = self.client.post("/products", data="Not JSON")
        self.assertEqual(response.status_code, status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)
