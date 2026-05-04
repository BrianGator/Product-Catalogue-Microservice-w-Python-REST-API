import unittest
from service import app
from service.models import Product, db
from service.common import status

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        with app.app_context():
            db.drop_all()
            db.create_all()

    def test_api_to_db_persistence(self):
        """Verify API created data is queryable via Model"""
        payload = {
            "name": "Int-Test-Product",
            "description": "Integration verification",
            "price": "99.99",
            "available": True,
            "category": "TOOLS"
        }
        # Step 1: POST via API
        self.client.post("/products", json=payload)
        
        # Step 2: Query via Model
        product = Product.find_by_name("Int-Test-Product").first()
        self.assertIsNotNone(product)
        self.assertEqual(product.price, 99.99)
