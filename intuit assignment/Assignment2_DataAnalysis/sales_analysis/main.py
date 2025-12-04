from utils.csv_reader import CSVReader
from services.analyzer import SalesAnalyzer


def main():
    try:
        file_path = "sample_sales.csv"
        records = CSVReader.read_sales(file_path)

        print("Total Revenue:", SalesAnalyzer.total_revenue(records))
        print("Total Quantity:", SalesAnalyzer.total_quantity(records))
        print("Revenue By Region:", SalesAnalyzer.revenue_by_region(records))
        print("Top Selling:", SalesAnalyzer.top_selling_products(records))

    except FileNotFoundError:
        print("[ERROR] CSV file not found.")
    except Exception as e:
        print("[ERROR] Unexpected error:", e)


if __name__ == "__main__":
    main()
 