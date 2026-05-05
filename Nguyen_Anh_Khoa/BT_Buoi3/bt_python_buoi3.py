#1.Chuoi text="  hello world  "
text = "  hello world  "
#Dùng len() để đếm số ký tự (bao gồm cả khoảng trắng).
print(len(text))
#Dùng strip() để bỏ khoảng trắng đầu và cuối, sau đó in lại chiều dài.
text = text.strip()
print(len(text))

# 2. Cho chuỗi:  name = "Khoa"
name = "anh Khoa"
# In ra chữ hoa toàn bộ.
print(name.upper())
# In ra chữ thường toàn bộ.
print(name.lower())
# In ra dạng capitalize (chữ cái đầu viết hoa).
print(name.capitalize())
# In ra dạng title (mỗi từ viết hoa chữ cái đầu).
print(name.title())
 	
# 3. Viết chương trình cắt chuỗi:
s = "Automation Testing"
# Lấy ra từ "Automation".
print(s[0:10])
# Lấy ra từ "Testing".
print(s[11:18])
# Lấy 5 ký tự đầu tiên.
print(s[:5])
# Lấy 3 ký tự cuối cùng.
print(s[-3:])
 	
# 4. Cho chuỗi số điện thoại:
messy_phone = " 090-123 4567 "
# Dùng strip() để bỏ khoảng trắng.
print(messy_phone.strip())
# Dùng replace() để bỏ dấu - và khoảng trắng.
# In ra số điện thoại chuẩn hóa: 0901234567.
print(messy_phone.replace("-","").replace(" ",""))
 	
# 5. Cho list:
fruits = ["apple", "banana", "cherry"]
# Dùng join() để nối list thành một chuỗi dạng: "apple, banana, cherry".
fruits = ",".join(fruits)
print(fruits)
 	
# 6. Cho chuỗi log:
log = "ERROR: Login failed at 10:45"
# Kiểm tra trong log có chứa từ "ERROR" hay không (dùng in).
checkError = "ERROR"
# Nếu có, in ra: "❌ Có lỗi xảy ra".
# Nếu không, in ra: "✅ Hệ thống bình thường".
if checkError in log:
    print("❌ Có lỗi xảy ra")
else:
    print("✅ Hệ thống bình thường")