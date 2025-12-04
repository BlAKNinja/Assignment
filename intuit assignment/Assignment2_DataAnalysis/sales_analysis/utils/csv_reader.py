import csv
import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, ROOT)
from  models.sale_record import SaleRecord


class CSVReader:
    """
    Reads CSV file and converts each row into a SaleRecord object.
    """

    @staticmethod
    def read_sales(file_path):
        records = []
        with open(file_path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                record = SaleRecord(
                    row["date"],
                    row["region"],
                    row["product"],
                    row["quantity"],
                    row["price"]
                )
                records.append(record)
        return records
