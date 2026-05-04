class Calculator:

    def Add(self, a, b):
        return a + b

    def Subtract(self, a, b):
        return a - b

    def Multiply(self, a, b):
        return a * b

    def Divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Không thể chia cho 0")
        else:
            return a / b
        
calc = Calculator()
print(calc.Add(5, 3))        
print(calc.Subtract(5, 3))  
print(calc.Multiply(5, 3))   
print(calc.Divide(5, 3))     
print(calc.Divide(5, 0))    

'''
Không có __init__() vì nó sẽ mặc định pass, không có thuộc tính nào cần khởi tạo khi tạo đối tượng Calculator.
Các phương thức Add, Subtract, Multiply, Divide thực hiện các phép toán tương ứng trên hai số a và b.
'''