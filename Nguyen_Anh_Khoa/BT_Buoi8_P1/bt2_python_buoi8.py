# Bài 2: Máy tính đơn giản Viết một class Calculator.
# Không cần __init__ phức tạp.
# Phương thức add(a, b): Trả về tổng của a và b.
# Phương thức subtract(a, b): Trả về hiệu của a và b.
# Phương thức multiply(a, b): Trả về tích của a và b.
# Phương thức divide(a, b): Trả về thương của a và b. Dùng try-except để xử lý trường hợp b bằng 0.

class Calculator():
    def add(self, a, b):
        return a+b

    def subtract(self, a, b):
        return a-b

    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Can't devide by zero.")
        else:
            return a/b
        
calc = Calculator()
print(f"Add: {calc.add(10,5)}")
print(f"Subtract: {calc.subtract(10,4)}")
print(f"Multiply: {calc.multiply(10,2)}")
print(f"Devide: {calc.divide(10,0)}")