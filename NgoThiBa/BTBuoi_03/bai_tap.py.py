# #Bài tập 1:
# text = " hello world "
# length_1 = len(text)
# print(f"Độ dài của chuỗi là: {length_1}")   #Dùng len() để đếm số ký tự (bao gồm cả khoảng trắng).

# print(text.strip()) #Dùng strip() để bỏ khoảng trắng đầu và cuối
# length_2 = text.strip()
# length_2 = len(length_2)
# print(f"Độ dài của chuỗi sau khi strip là: {length_2}") #In chiều dài sau khi strip

# #Bai tap 2: 
# name = "Ngô Thị Ba"
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.title())

# #Bài tập 3: 
# s = "Automation Testing"
# print(s[:10])
# print(s[11:])
# print(s[0:5])
# print(s[-3:])

# #Bài tập 4:
messy_phone = " 090-123 4567 "
phone_1 = messy_phone.strip()
phone_2 = messy_phone.replace(" ", "").replace("-","")
print(f"Số điện thoại chuẩn hóa là: {phone_2}")

# #Bài tập 5: 
fruits = ["apple", "banana", "cherry"]
fruits_1 = ",".join(fruits)
print(fruits_1)

#Bài tập 6:
log = "ERROR: Login failed at 10:45"
if "ERRORs" in log:   #Kiểm tra trong log có chứa từ "ERROR" hay không (dùng in).
    print("❌ Có lỗi xảy ra")
else:
    print( "✅ Hệ thống bình thường")

    




