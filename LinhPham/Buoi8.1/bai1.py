class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
       return self.price * self.quantity
         
    
    def display_info(self):
        print(f"San pham: {self.name}, Don gia: {self.price}, so luong: {self.quantity}, tong gia tri{self.get_total_price()}")

product1 = Product("iphone", 10, 50)
product1.display_info()
