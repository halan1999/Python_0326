# Nhập chia 2 số a và b
# Nếu b bằng không, in ra không thể chia cho 0
# Nếu b lớn hơn a, in ra là phi logic
# Và ngược lại in ra kết quả a/b
# Cuối cùng là in ra thông báo "Hoàn thành"

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    if b == 0:
        raise ValueError("B cannot is 0")
    elif b > a:
        raise ValueError ("It's non-logic")
except ValueError as mess:
    print(mess)
else:
    print("the result is: ", a/b)
finally:
    print("Done")

