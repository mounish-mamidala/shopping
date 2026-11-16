class ShoppingCart:

    def __init__(self):
        self.items = {}

    def add_item(self, product, price, quantity=1):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        self.items[product] = self.items.get(product, 0) + quantity
        print(f"{product} added to cart")

    def remove_item(self, product):
        if product in self.items:
            del self.items[product]
            print(f"{product} removed from cart")
        else:
            print("Product not found")

    def view_cart(self):
        return self.items