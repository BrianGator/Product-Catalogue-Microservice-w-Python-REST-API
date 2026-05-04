import unittest
import os
from decimal import Decimal
from service.models import Product, Category, db, DataValidationError
from service import app
from tests.factories import ProductFactory

DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///../development.db")

class TestProductModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
        Product.init_db(app)

    def test_create_a_product(self):
        product = Product(name="Fedora", price=Decimal("12.50"), category=Category.CLOTHS)
        product.create()
        self.assertIsNotNone(product.id)

    def test_find_by_name(self):
        ProductFactory(name="Widget").create()
        found = Product.find_by_name("Widget")
        self.assertEqual(found[0].name, "Widget")
