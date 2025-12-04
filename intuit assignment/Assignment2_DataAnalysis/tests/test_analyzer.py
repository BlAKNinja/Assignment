import unittest
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, ROOT)

from sales_analysis.models.sale_record import SaleRecord
from sales_analysis.services.analyzer import SalesAnalyzer


class TestSalesAnalyzer(unittest.TestCase):

    def setUp(self):
        # reusable sample list of records
        self.records = [
            SaleRecord("2024", "North", "Phone", 2, 500),
            SaleRecord("2024", "North", "Laptop", 1, 1000),
            SaleRecord("2024", "South", "Phone", 3, 500),
        ]

    def test_total_revenue(self):
        # verifies reduce-based revenue sum
        result = SalesAnalyzer.total_revenue(self.records)
        self.assertEqual(result, (2*500) + (1*1000) + (3*500))

    def test_total_quantity(self):
        # verifies reduce-based quantity sum
        result = SalesAnalyzer.total_quantity(self.records)
        self.assertEqual(result, 2 + 1 + 3)

    def test_group_by_region(self):
        # ensures sorted grouping using itertools.groupby
        groups = SalesAnalyzer.group_by_region(self.records)
        self.assertEqual(len(groups["North"]), 2)
        self.assertEqual(len(groups["South"]), 1)

    def test_revenue_by_region(self):
        # validates region-wise revenue aggregation
        rev = SalesAnalyzer.revenue_by_region(self.records)
        self.assertEqual(rev["North"], 2000)
        self.assertEqual(rev["South"], 1500)

    def test_top_selling_products(self):
        # verifies product revenue sorting
        top = SalesAnalyzer.top_selling_products(self.records, top_n=1)
        self.assertEqual(top[0][0], "Phone")
