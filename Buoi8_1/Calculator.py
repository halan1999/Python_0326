class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Cannot divide by zero"

# Sử dụng
calc = Calculator()
print(calc.add(3, 5))
print(calc.sub(10, 4))
print(calc.mul(6, 7))   
print(calc.div(10, 0))