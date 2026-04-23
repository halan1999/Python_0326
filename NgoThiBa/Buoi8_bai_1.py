class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
    def get_total_price(self):
        return self.price * self.quantity
        
    def display_infor(self):  
        total = self.get_total_price() 
        print (f"Sản phẩm {item_1.name}, Đơn giá {item_1.price}, số lượng {item_1.quantity}, Tổng giá trị: {total}")
item_1 = Product (name = "Orange", price = 15.6, quantity = 2) 
item_1.display_infor()