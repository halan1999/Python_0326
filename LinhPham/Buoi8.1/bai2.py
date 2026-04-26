
class Calculator:
    def add(self, a, b, c):
        return a + b + c
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
        
    def divide(self, a, b):
        try:
            return a / b    
        except ZeroDivisionError as mess:
            print(f"Error: {mess}")

cal1 = Calculator()
print(f"Tong {cal1.add(3, 4, 5)}")
print(f"Hieu {cal1.subtract(3, 4)}")
print(f"Tich {cal1.multiply(3, 4)}")
print(f"Thuong {cal1.divide(3, 0)}")