class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f" Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def get_total_price(self):
        return self.price * self.quantity
# Example usage
product1 = Product("Laptop", 1000, 2)
product1.display_info()
print(f"Total Price: {product1.get_total_price()}")