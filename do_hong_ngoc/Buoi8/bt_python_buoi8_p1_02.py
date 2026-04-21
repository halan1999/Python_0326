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
        except ZeroDivisionError:
            return "Không thể chia cho 0"
        
calc = Calculator()
print(calc.add(5, 3))        
print(calc.divide(10, 0))    