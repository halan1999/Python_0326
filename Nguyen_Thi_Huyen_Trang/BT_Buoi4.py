#1. Tìm kiếm sản phẩm trong list sản phẩm sau
products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]
# Viết chương trình duyệt danh sách và kiểm tra xem "MacBook Pro 16 inch" có tồn tại không.
# Nếu có → in "Đã tìm thấy sản phẩm" và dừng vòng lặp (break).
# Nếu không → in "Không tìm thấy sản phẩm".
for product in products:
    if product == "MacBook Pro 16 inch":
        print("Đã tìm thấy sản phẩm")
        break
else:
    print("Không tìm thấy sản phẩm")

#2. Cho list số sau
numbers = [2, 5, 8, 11, 14, 17, 20]
#In ra tất cả số trong list.
for number in numbers:
    print(number)
# In ra số chẵn trong list.
for number in numbers:
    if number % 2 == 0:
        print(number)
# Tính tổng tất cả số trong list.
i = 0
for n in numbers:
    i += n    
print("Tổng =", i)
# In ra bảng cửu chương của từng số trong list (gợi ý: dùng for i in range(1, 11):) (bài tập nâng cao dùng for trong for, có thể làm hoặc không)
numbers = [2, 5, 8, 11, 14, 17, 20]
for a in numbers:
    for b in range(1,11):
        print(f"Bảng cửu chương của {a}, {a} * {b} = {a*b}")
    
    