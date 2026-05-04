class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def get_total_price(self):
        return self.price * self.quantity
    
    def display_info(self):
        print(f"Sản phẩm: {self.name}, Đơn giá: {self.price}, Số lượng: {self.quantity}, Tổng giá: {self.get_total_price()}")
product1 = Product("Mobile phone", 2300000, 2)
product1.display_info()