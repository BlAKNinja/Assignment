import unittest
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, ROOT)

from sales_analysis.models.sale_record import SaleRecord


class TestSaleRecord(unittest.TestCase):

    def test_record_fields_and_total(self):
        # verifies attribute assignment and total calculation
        r = SaleRecord("2024", "North", "Phone", 2, 500)
        self.assertEqual(r.date, "2024")
        self.assertEqual(r.region, "North")
        self.assertEqual(r.product, "Phone")
        self.assertEqual(r.quantity, 2)
        self.assertEqual(r.price, 500.0)
        self.assertEqual(r.total, 1000)

    def test_record_repr(self):
        # ensures repr returns expected printable form
        r = SaleRecord("2024", "North", "Phone", 2, 500)
        self.assertIn("SaleRecord", repr(r))
