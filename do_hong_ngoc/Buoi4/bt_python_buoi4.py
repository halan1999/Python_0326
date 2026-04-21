#Bài 1: Kiểm tra message đăng nhập
expected_messages = ["Login succesfull", "Welcome"]
actual_message = "Welcome"

if actual_message in expected_messages:
    print("Message valid")
else:
    print("Message invalid")


#Bài 2: Tìm số chia hết cho 7 đầu tiên (1 → 100)

for i in range(1, 101):
    if i % 7 == 0:
        print("Số đầu tiên chia hết cho 7 là:", i)
        break



#Bài 3: Phân loại học lực

scores = [95, 82, 67, 45, 88, 90, 50]

for score in scores:
    if score >= 90:
        print(score, "-> Xuất sắc")
    elif score >= 70:
        print(score, "-> Khá")
    elif score >= 50:
        print(score, "-> Trung bình")
    else:
        print(score, "-> Yếu")



#Bài 4: Bảng cửu chương 2 & 3
for n in [2, 3]:
    print(f"\nBảng cửu chương {n}:")
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")


#BÀI TẬP CHUNG

#Bài 1: Tìm kiếm sản phẩm
products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]

found = False

for product in products:
    if product == "MacBook Pro 16 inch":
        print("Đã tìm thấy sản phẩm")
        found = True
        break

if not found:
    print("Không tìm thấy sản phẩm")



#Bài 2: Làm việc với list số

numbers = [2, 5, 8, 11, 14, 17, 20]

# In tất cả số
print("Tất cả số:")
for num in numbers:
    print(num)

# In số chẵn
print("\nSố chẵn:")
for num in numbers:
    if num % 2 == 0:
        print(num)

# Tính tổng
total = sum(numbers)
print("\nTổng:", total)


#BT nâng cao
for num in numbers:
    print(f"\nBảng cửu chương của {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")







