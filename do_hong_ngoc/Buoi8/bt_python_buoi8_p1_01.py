class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity

    def display_info(self):
        total = self.get_total_price()
        print(f"Sản phẩm: {self.name}, Đơn giá: {self.price}, "
              f"Số lượng: {self.quantity}, Tổng giá trị: {total}")
        

p1 = Product("Laptop", 1500, 2)
p1.display_info()