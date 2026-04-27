#Câu 1
text = "  hello world  "

# Đếm số ký tự (có khoảng trắng)
print(len(text))

# Bỏ khoảng trắng đầu và cuối rồi đếm lại
print(len(text.strip()))


#Câu 2
name = "Do hoNG Ngoc"

print(name.upper())       # Viết hoa toàn bộ
print(name.lower())       # Viết thường toàn bộ
print(name.capitalize())  # Viết hoa chữ cái đầu
print(name.title())       # Mỗi từ viết hoa chữ cái đầu


#Câu 3
s = "Automation Testing"

# Lấy "Automation"
print(s[:10:])

# Lấy "Testing"
print(s[11::])

# Lấy 5 ký tự đầu
print(s[:5:])

# Lấy 3 ký tự cuối
print(s[-3::])



#Câu 4
messy_phone = " 090-123 4567 "

# Bỏ khoảng trắng đầu cuối
print(messy_phone.strip())

# Xóa dấu "-" và khoảng trắng

phone = phone.replace("-", "").replace(" ", "")

print(phone)



#Câu 5
fruits = ["apple", "banana", "cherry"]

result = ", ".join(fruits)

print(result)





#Câu 6
log = "ERROR: Login failed at 10:45"

if "ERROR" in log:
    print("Có lỗi xảy ra")
else:
    print("Hệ thống bình thường")