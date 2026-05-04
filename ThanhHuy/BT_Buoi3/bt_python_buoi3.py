#Bai 1
text = "  hello world  "
print(f"Độ dài của chuỗi bao gồm khoảng trắng là: {len(text)}")
updated_text = text.strip()
print(f"Độ dài của chuỗi sau khi bỏ khoảng trắng đầu và cuối là : {len(updated_text)}")

#Bai 2
name = "nguyen thanh huy"
print(f"In tên chữ hoa toàn bộ: {name.upper()}")
print(f"In tên chữ thường toàn bộ: {name.lower()}")
print(f"In tên chữ cái đầu viết hoa: {name.capitalize()}")
print(f"In tên mỗi từ viết hoa chữ cái đầu: {name.title()}")

#bai 3
s = "Automation Testing"
print(s[:10:])
print(s[11::])
print(f"5 kí tự đầu là: {s[:5:]}")
print(f"3 kí tự cuối là: {s[15::]}")

#Bai 4
messy_phone = " 090-123 4567 "
a = messy_phone.strip().replace("-","").replace(" ","")
print(a)

#bai 5
fruits = ["apple", "banana", "cherry"]
updated_join = ",".join(fruits)
print(updated_join)

#Bai 6
log = "ERROR: Login failed at 10:45"
errorKeys = "ERROR"
if errorKeys in log:
    print("❌ Có lỗi xảy ra")
else:
    print("✅ Hệ thống bình thường")