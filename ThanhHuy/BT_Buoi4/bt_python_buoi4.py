#Bai 1
expected_messages =["Login succesfull", "Welcome"]      
actual_message = "Welcome"
if actual_message in expected_messages:
    print("Message valid")
else:
    print("Message invalid")

#Bai 2
for i in range (1,101):
    if (i%7 == 0):
        print(f"Số chia hết cho 7 đầu tiên là: {i}")
        break

#Bai 3
scores =[95, 82, 67, 45, 88, 90, 50]
dtb = sum(scores)/len(scores)
if dtb >= 90:
    print("Xuất sắc")
elif dtb >=70:
    print("Khá")
elif dtb >= 50:
    print("Trung bình")
else:
    print("Yếu")

#bai 4
for i in range(2,4):
    print(f"Bảng cửu chương {i}")
    for x in range(1,11):
        print(f"{i} * {x} = {i*x}")

#Bai tap chung
#Bai 1
products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]
product = "MacBook Pro 16 inch"
for product in products:
    print("Đã tìm thấy sản phẩm")
    break
else:
    print("Không tìm thấy sản phẩm")

#Bai2
numbers = [2, 5, 8, 11, 14, 17, 20]
print("Tất cả số trong list là ", numbers)
print("Tổng tất cả số trong list là: ", sum(numbers))
for i in numbers:
    
    if (i %2 == 0):
        print(f"Số chẵn trong list là: {i}")
for i in numbers:
    print(f"Bảng cửu chương {i}")
    for x in range(1,11):
        print(f"{i} * {x} = {i*x}")