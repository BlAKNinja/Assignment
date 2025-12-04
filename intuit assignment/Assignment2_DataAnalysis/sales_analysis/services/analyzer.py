from itertools import groupby
from functools import reduce


class SalesAnalyzer:
    """
    Performs functional-style data analysis on a list of SaleRecord objects.
    """

    @staticmethod
    def total_revenue(records):
        return reduce(lambda acc, r: acc + r.total, records, 0)

    @staticmethod
    def total_quantity(records):
        return reduce(lambda acc, r: acc + r.quantity, records, 0)

    @staticmethod
    def group_by_region(records):
        # sorted first because itertools.groupby requires sorted input
        sorted_records = sorted(records, key=lambda r: r.region)
        return {
            region: list(group) 
            for region, group in groupby(sorted_records, key=lambda r: r.region)
        }

    @staticmethod
    def revenue_by_region(records):
        groups = SalesAnalyzer.group_by_region(records)
        return {
            region: sum(r.total for r in recs)
            for region, recs in groups.items()
        }

    @staticmethod
    def top_selling_products(records, top_n=3):
        """
        Returns top N products by revenue.
        """
        product_map = {}

        for r in records:
            product_map.setdefault(r.product, 0)
            product_map[r.product] += r.total

        sorted_products = sorted(product_map.items(), key=lambda x: x[1], reverse=True)
        return sorted_products[:top_n]
