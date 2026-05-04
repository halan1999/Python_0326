#Bai1
products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]

found = False

for product in products:  
    if product == "MacBook Pro 16 inch":
        print('Đã tìm thấy sản phẩm')
        found = True
        break
if not found:
        print('Không tìm thấy sản phẩm')
        
#Bai2
numbers = [2, 5, 8, 11, 14, 17, 20]

# In ra tất cả số trong list.
for number in numbers:
    print(number)
        
# In ra số chẵn trong list.
for so_chan in numbers:
    if(so_chan % 2 == 0):
        print(so_chan) 

# Tính tổng tất cả số trong list.
total = sum(numbers)
print(total)

# In ra bảng cửu chương của từng số trong list (gợi ý: dùng for i in range(1, 11):)
for i in numbers:
    print(f"\nbảng cửu chương {i}")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
