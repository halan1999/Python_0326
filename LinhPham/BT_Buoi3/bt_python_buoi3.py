# CÂU 1
text = "  hello world  "
lengh = len(text)
print(text.strip())

# CÂU 2
name = "Phạm Hoài Linh"
#Toàn bộ chữ hoa
print(name.upper())

#Toàn bộ chữ thường
print(name.lower())

#Chữ cái đầu viết hoa
print(name.capitalize())

#Mỗi từ viết hoa chữ cái đầu
print(name.title())

# CÂU 3
s = "Automation testing"

# Lấy ra từ "Automation"
print(s[:10:])

# Lấy ra từ "Testing"
print (s[11::])

# Lấy 5 ký tự đầu tiên
print(s[:5:])

#Lấy ra 3 ký tự cuối cùng
print (s[15::])

# CÂU 4
messy_phone = " 090-123 4567 "

#Bo khoang trang
print(messy_phone.strip())

#Dung replace thay the khoang trang và -
print(messy_phone.replace("-","",).replace(" ",""))


# CÂU 5 
fruits = ["apple", "banana", "cherry"]
print( ", ".join(fruits))


# CÂU 6
log = "ERROR: Login failed at 10:45"
if "ERROR" in log:
    print("X có lỗi xãy ra")
else:
    print("Hệ thống bình thường")