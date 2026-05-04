# Bài 1: Lớp Product (Sản phẩm) Viết một class Product để quản lý thông tin sản phẩm.

# - __init__: Nhận vào name, price, và quantity (số lượng).
# - Phương thức get_total_price(): Trả về tổng giá trị của sản phẩm đó (price * quantity).
# - Phương thức display_info(): In ra thông tin sản phẩm theo định dạng: "Sản phẩm: [Tên], Đơn giá: [Giá], Số lượng: [Số lượng], Tổng giá trị: [Tổng giá trị]".

class SanPham:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity
    def display_info(self):
        print(f"Sản phẩm: {self.name}, Đơn giá: {self.price}, Số lượng: {self.quantity}, Tổng giá trị: {self.get_total_price()}" )

p1 = SanPham(name ="Laptop", price = 30000000, quantity = 2)
p1.display_info()

# Máy tính đơn giản Viết một class Calculator.
# Không cần __init__ phức tạp.
# Phương thức add(a, b): Trả về tổng của a và b.
# Phương thức subtract(a, b): Trả về hiệu của a và b.
# Phương thức multiply(a, b): Trả về tích của a và b.
# Phương thức divide(a, b): Trả về thương của a và b. Dùng try-except để xử lý trường hợp b bằng 0.

class Calculator:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def add(self):
        print(f"Sum of {self.a} and {self.b} is: {self.a + self.b}")
    def subtract(self):
        print(f"Subtract of {self.a} and {self.b} is: {self.a - self.b}")
    def multiply(self):
        print(f"Multiply of {self.a} and {self.b} is: {self.a * self.b}")
        
    def divide(self):
        try:
            print(f"Divide of {self.a} and {self.b} is: {self.a / self.b}")
        except ZeroDivisionError:
            print(f"Can't divide for 0")

# 1. Tạo đối tượng và truyền giá trị ban đầu vào
my_cal = Calculator(7, 5) 

# 2. Gọi các hàm từ đối tượng vừa tạo (không truyền số vào đây nữa)
my_cal.add()
my_cal.subtract()
my_cal.multiply()
my_cal.divide()





