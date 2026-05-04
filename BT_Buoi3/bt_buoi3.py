# 1. Cho chuỗi:
#  text = "  hello world  "
# Dùng len() để đếm số ký tự (bao gồm cả khoảng trắng).
# Dùng strip() để bỏ khoảng trắng đầu và cuối, sau đó in lại chiều dài.
text = "  hello world  "
print(len(text))
text_stripped = text.strip()
print(len(text_stripped))

 	
# 2. Cho chuỗi:  name = "tên bạn"
# In ra chữ hoa toàn bộ.
# In ra chữ thường toàn bộ.
# In ra dạng capitalize (chữ cái đầu viết hoa).
# In ra dạng title (mỗi từ viết hoa chữ cái đầu).
name = "minh tue"
name1 = "MINH TUE"
print (name.upper())
print (name1.lower())
print (name.capitalize())
print (name.title())
#bài 3
s = "Automation Testing"
s1 = s[0:10:1]
print(s1) #lấy  ra "Automation"
s2 = s[11:18:1]
print(s2) #lấy  ra "Testing"
s3 = s[:5]
# print(s3) #lấy  ra 5 ký tự đầu
s4 = s[-3:]
print(s4) #lấy  ra 3 ký tự cuối
#bài 4
messy_phone= " 090-123 4567 "
phone = messy_phone.strip() #dùng strip bỏ khoảng trắng đầu và cuối
print(phone) 
# #Dùng replace() để bỏ dấu - và khoảng trắng & in số điện thoại chuẩn hóa
print(phone.replace("-", "").replace(" ", ""))
#bài 6
log = "ERROR: Login failed at 10:45"
if ("ERROR" in log):
    print ("Có lỗi xảy ra")
else:
    print ("Không có lỗi nào")
