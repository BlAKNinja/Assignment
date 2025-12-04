class SaleRecord:
    """
    Represents a single row of sales data.
    Example CSV fields:
    date, region, product, quantity, price
    """

    def __init__(self, date, region, product, quantity, price):
        self.date = date
        self.region = region
        self.product = product
        self.quantity = int(quantity)
        self.price = float(price)

    @property
    def total(self):
        return self.quantity * self.price

    def __repr__(self):
        return f"SaleRecord({self.date}, {self.region}, {self.product}, {self.quantity}, {self.price})"