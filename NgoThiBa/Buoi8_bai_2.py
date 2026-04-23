class Calculator:
    # def __init__(self, a:int, b:int):
    #     self.a = a
    #     self.b = b
        
    def add (self, a,b):
        return a + b
    def subtract (self,a,b):
        return a - b
    def multiply (self,a,b):
        return a * b
    def divide (self,a,b):
        if b == 0:
            raise ValueError ("Không chia hết cho 0")
        else:
            return a / b
        
calculator_1 = Calculator()
print(f"Tổng là:", calculator_1.add(1,2))
print(f"Trừ là", calculator_1.subtract(5,2))
print (f"Nhân là", calculator_1.multiply (3,3))
print (f"Chia là: ", calculator_1.divide(3,0))