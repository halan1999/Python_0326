#Bài 1: Nhập số
try:
    number = int(input("Nhập một số: "))
    print("Bình phương là:", number ** 2)
except ValueError:
    print("Sai định dạng")


#Bài 2: File
try:
    with open("data.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File không tồn tại")
finally:
    print("Kết thúc chương trình")



#Bài 3: Xử lý ValueError + raise
from datetime import datetime

current_year = datetime.now().year

try:
    birth_year = int(input("Nhập năm sinh: "))
    
    if birth_year > current_year:
        raise ValueError("Năm sinh không thể lớn hơn năm hiện tại.")
    
except ValueError as e:
    print("Lỗi:", e)

else:
    age = current_year - birth_year
    print("Tuổi của bạn là:", age)
