#1.Tim kiem san pham trong list san pham sau
products = ["iPhone13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]
#Duyet danh sach va kiem tra xem "MacBook Pro 16 inch" co ton tai khong
product = "MacBook Pro 16 inch"
if product in products:
    print("Da tim thay san pham")
else:
    print("Khong tim thay san pham")

#2.Cho list so sau
numbers = [2, 5, 8, 11, 14, 17, 20]
#In ra tat ca so trong list
for num in numbers:
    print(num)
#In ra so chan trong list
for num in numbers:
    if(num % 2 ==0):
        print(num)
#Tinh tong tat ca so trong list
total = sum(numbers)
print(total)
#In ra bang cuu chuong cua tung so trong list
for num in numbers:
    print(f"\nBảng cửu chương của {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")
