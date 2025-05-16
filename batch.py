from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from product import Product

class GeneralBatch:
    def __init__(self, bcode, quantity):
        self.bcode = bcode
        self.quantity = quantity
        self.products: list["Product"] = []

    def add_product(self, prod: "Product"):
        if prod not in self.products:
            self.products.append(prod)

    def remove_product(self, prod: "Product"):
        if prod in self.products:
            self.products.remove(prod)
        else:
            print(f"Product {prod} not found")
