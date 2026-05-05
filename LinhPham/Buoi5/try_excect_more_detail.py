# Viết chương trình chia 2 số a và b do người dùng nhập. Dùng try-except riêng biệt để bắt lỗi ValueError (nếu nhập chữ) 
# và ZeroDivisionError (nếu chia cho 0) với các thông báo lỗi tương ứng.

# Cách 1
# try:
#     a = int(input("Please enter a value: "))
#     b = int(input("Please enter b value: "))
#     print("The result of dividing a and b is: ", a/b)
# except ValueError:
#     print ("Please enter an inter value")
# except ZeroDivisionError:
#     print ("Cannot enter 0")


# Cách 2 
# try:
#     c = int(input("Please enter a value: "))
#     d = int(input("Please enter b value: "))
#     print("The result of dividing a and b is: ", c/d)
# except (ValueError, ZeroDivisionError) as mess:
#     print("Error:", mess)

# 2 cách trên là trong trường hình mình dự đoán được lỗi nó có thể xãy ra, trong trường hợp không biết có thể xãy ra những lỗi nào
# nữa thì dùng hàm "Exception"
try:
    e = int(input("Please enter a value: "))
    f = int(input("Please enter b value: "))
    print("The result of dividing a and b is: ", e/f)
except Exception as ErrorMess:
    print("Error:", ErrorMess)