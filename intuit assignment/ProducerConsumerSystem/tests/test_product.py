import unittest
import os
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
from producer_consumer.models.product import Product


class TestProduct(unittest.TestCase):

    def test_product_attributes_and_repr(self):
        """Product should store ID and return clean repr string."""
        p = Product("X1")
        self.assertEqual(p.product_id, "X1")
        self.assertEqual(repr(p), "Product(id=X1)")
