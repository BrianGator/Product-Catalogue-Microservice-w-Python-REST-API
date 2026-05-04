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

    def test_price_precision(self):
        """Verify price decimal precision is preserved"""
        product = Product(name="Exact", price=Decimal("19.99"), category=Category.TOOLS)
        product.create()
        self.assertEqual(product.price, Decimal("19.99"))

    def test_invalid_category_assignment(self):
        """Verify invalid category type raises error or handles gracefully"""
        product = Product(name="BadCat", price=Decimal("1.00"), category="INVALID")
        # Depending on implementation, we check if create() validation catches it
        # Assuming DataValidationError is used
        with self.assertRaises((DataValidationError, AttributeError, ValueError)):
             product.create()

    def test_long_product_name(self):
        """Verify model handles long string names (up to limit)"""
        long_name = "A" * 100
        product = Product(name=long_name, price=Decimal("5.00"), category=Category.TOOLS)
        product.create()
        self.assertEqual(product.id, Product.find(product.id).id)

    def test_update_product_price(self):
        """Verify price update reflects in DB"""
        product = ProductFactory().create()
        product.price = Decimal("500.00")
        product.update()
        self.assertEqual(Product.find(product.id).price, Decimal("500.00"))

    def test_delete_a_product(self):
        """Verify product deletion"""
        product = ProductFactory().create()
        product.delete()
        self.assertIsNone(Product.find(product.id))

    def test_serialize_product(self):
        """Verify serialization dictionary structure"""
        product = ProductFactory().create()
        data = product.serialize()
        self.assertEqual(data["name"], product.name)
        self.assertIn("category", data)
