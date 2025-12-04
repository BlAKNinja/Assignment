import unittest
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, ROOT)

from sales_analysis.utils.csv_reader import CSVReader
from sales_analysis.services.analyzer import SalesAnalyzer


class TestSystemFlow(unittest.TestCase):

    def test_full_pipeline(self):
        # writes a short CSV and runs full read → analyze flow
        path = "tests/flow_data.csv"
        with open(path, "w") as f:
            f.write("date,region,product,quantity,price\n")
            f.write("2024,North,Phone,2,500\n")
            f.write("2024,South,Laptop,1,1000\n")

        records = CSVReader.read_sales(path)

        total_rev = SalesAnalyzer.total_revenue(records)
        rev_by_region = SalesAnalyzer.revenue_by_region(records)
        top = SalesAnalyzer.top_selling_products(records, 1)

        # validate pipeline output
        self.assertEqual(total_rev, 2000)
        self.assertEqual(rev_by_region["North"], 1000)
        self.assertEqual(rev_by_region["South"], 1000)
        self.assertEqual(top[0][0], "Phone")
