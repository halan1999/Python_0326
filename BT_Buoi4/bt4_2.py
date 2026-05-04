#bài 1.
products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]
for product in products:
    if product == "MacBook Pro 16 inch":
        print("Đã tìm thấy sản phẩm")
        break
else:
        print("Không tìm thấy sản phẩm")
#bài 2
numbers = [2, 5, 8, 11, 14, 17, 20]
#In từng số trong danh sách
for number in numbers:
      print (number)
#In từng số chẵn trong danh sách
for number in numbers:
    if number % 2 == 0:
        print( f"{number} là số chẵn")
#Tổng các số trong danh sách
total = 0 
for number in numbers:
    total += number
print(f"Tổng các số trong danh sách là: {total}")
#Bảng cửu chương từng số trong danh sách 
for number in numbers:
    print (f"bảng cửu chương của {number}:")
    for i in range (1,11):
        print(f"{number} x {i} = {number*i}")
