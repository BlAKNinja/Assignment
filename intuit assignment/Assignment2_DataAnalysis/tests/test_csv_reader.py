import unittest
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, ROOT)

from sales_analysis.utils.csv_reader import CSVReader
from sales_analysis.models.sale_record import SaleRecord


class TestCSVReader(unittest.TestCase):

    def setUp(self):
        # temp csv file for tests
        self.file = "tests/temp_sales.csv"
        with open(self.file, "w") as f:
            f.write("date,region,product,quantity,price\n")
            f.write("2024-01-01,North,Phone,2,500\n")
            f.write("2024-01-02,South,Laptop,1,1000\n")

    def test_read_sales(self):
        # verifies CSV rows are loaded and mapped to SaleRecord
        records = CSVReader.read_sales(self.file)
        self.assertEqual(len(records), 2)
        self.assertIsInstance(records[0], SaleRecord)
        self.assertEqual(records[0].product, "Phone")
