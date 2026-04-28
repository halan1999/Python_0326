#Bài tập 1:
try:
    a = int(input ("Nhap so a: "))
    print(f"Bình phương của a la: {a **2}")
except ValueError:
    print("Sai định dạng")
finally:
    print("Kết thúc")
    

#Bài tập 3: 
try:
    year_birth = int(input("Nhập năm sinh của bạn: "))
    so_tuoi = 2026 - year_birth
    if year_birth >= 2026:
        raise ValueError ("Năm sinh không thể lớn hơn năm hiện tại")
    
except ValueError as e:
    print(e)
else:
    print(f"Số tuổi của bạn là: {so_tuoi}")






