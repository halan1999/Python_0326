#bài 1:
try:
    a = float(input("Nhập số a: "))
    print(f"Bình phương của a là {a**2}")
except ValueError:
    print("Sai định dạng")
#bài 2

try:
    with open("data.txt", "r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("File không tồn tại")
finally:
    print("Kết thúc chương trình")
#Bài 3
from datetime import datetime

try:
    a = int(input("Nhập năm sinh của bạn: "))
    if a < 0:
            raise ValueError("Năm sinh không thể âm")
    elif a > datetime.now().year:
            raise ValueError("Năm sinh không thể lớn hơn năm hiện tại")
    b= datetime.now().year - a
    print(b)
except ValueError as e:
    print(f"Lỗi: {e}")
else:
    print(f"Tuổi của bạn là: {b}")