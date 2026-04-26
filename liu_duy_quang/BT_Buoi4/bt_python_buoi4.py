#Dành cho những bạn chưa làm
# 1. Kiểm trả message đăng nhập xem có nằm trong danh sách sau:
# expected_messages = [“Login succesfull”, “Welcome”]            
# actual_message = “Welcome”                                                                   
# Nếu actual message nằm trong expected_messages thì in ra “Message valid” ngược lại thì in ra “Message invalid”

expected_messages = ["Login succesfull", "Welcome"]       
actual_message = "Welcome"                    
                                                  
# if actual_message in expected_messages:
#     print("Message valid")
# else:
#     print("Message invalid")

#2.Tìm số chia hết cho 7 đầu tiên trong dãy từ 1 đến 100 và in ra màn hình

# for i in range(1,100,1):
#     if i % 7 == 0:
#         print("Số chia hết cho 7 là: ", i)
#         break

# 3. Phân loại học lực theo điểm trong list sau:                 
# scores =[95, 82, 67, 45, 88, 90, 50]
# Từ 90 điểm trở lên -> xuất sắc
#  => 70: Khá
# => 50: trung bình                 
# < 50 :Yếu

# scores =[95, 82, 67, 45, 88, 90, 50]
# dtb = sum(scores)/len(scores)
# if dtb >= 90:
#     print("xuất sắc")
# elif dtb >= 70:
#     print("Khá")
# elif dtb >= 50:
#     print("trung bình")
# else:
#     print("yếu")

# 4. In ra bảng cửu chương 2 & 3

# for i in range(1,11,1):
#     print("2 x ", i, "=", i * 2)

# for i in range(1,11,1):
#     print("3 x ", i, "=", i * 3)

# Bài tập chung
 	
# 1. Tìm kiếm sản phẩm trong list sản phẩm sau
# products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]
# Viết chương trình duyệt danh sách và kiểm tra xem "MacBook Pro 16 inch" có tồn tại không.
# Nếu có → in "Đã tìm thấy sản phẩm" và dừng vòng lặp (break).
# Nếu không → in "Không tìm thấy sản phẩm".

# products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]
# product = "MacBook Pro 16 inch"
# if product in products:
#     print("Đã tìm thấy sản phẩm")
# else:
#     print("Không tìm thấy sản phẩm")

# 2. Cho list số sau
# numbers = [2, 5, 8, 11, 14, 17, 20]
# In ra tất cả số trong list
# In ra số chẵn trong list.
# Tính tổng tất cả số trong list.
# In ra bảng cửu chương của từng số trong list (gợi ý: dùng for i in range(1, 11):) (bài tập nâng cao dùng for trong for, có thể làm hoặc không)

numbers = [2, 5, 8, 11, 14, 17, 20]
# print(numbers)

# for i in numbers:
#     if i % 2 == 0:
#         print("số chẵn là: ", i)

print("tổng", sum(numbers))
