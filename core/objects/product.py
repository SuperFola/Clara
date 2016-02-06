__author__ = 'Folaefolc'
"""
Code par Folaefolc
Licence MIT
"""


class Product:
    def __init__(self, name: str="", price: float=1.0, quality: float=1.0):
        self.name = name
        self.price = price
        self.quality = quality


class QuantifiedProduct(Product):
    def __init__(self, name: str="", price: float=1.0, quality: float=1.0, quantity: int=1):
        super().__init__(name, price, quality)
        self.quantity = quantity

    def construct_from_product(self, product: Product, quantity: int) -> object:
        """A second method to create a QuantifiedProduct based on a product"""
        self.name = product.name
        self.price = product.price
        self.quality = product.quality
        self.quantity = quantity
        return self