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


        
        





