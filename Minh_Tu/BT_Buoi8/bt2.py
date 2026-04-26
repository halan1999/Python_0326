class Calculator:
     
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        try:
            return a / b
        except ValueError as e:
            return e
            
calc = Calculator()
print('Tổng:', calc.add(5, 11))
print('Hiệu:', calc.subtract(3, 7))
print('Tích:', calc.multiply(4, 9))
print('Thương:', calc.divide(2, 0))