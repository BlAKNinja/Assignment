
# Product Model


class Product:
    # Product represents the data object used inside the producer–consumer workflow.

    def __init__(self, product_id: str):
        # param product_id: Unique identifier for the product.

        self.product_id = product_id

    def __repr__(self):
        return f"Product(id={self.product_id})"
