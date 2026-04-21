class Product:
    def __init__(self, name : str, price : float, quantity : int):
        self.name = name
        self.price = price
        self.quantity = quantity
        
    def get_total_price(self):
        return self.price * self.quantity
       
    
    def display_info(self):
        total = self.get_total_price()
        print(f"Sản phẩm: {self.name}, Đơn giá: {self.price}, Số lượng: {self.quantity}, Tổng giá trị: {total}")
        
product1 = Product('Samsung', 15.500, 10)
product1.display_info()