# #Cau1
# text = "  hello world  "
# print(len(text))

# text2 = text.strip()
# print(len(text2))

# #Cau2
# name = "Liu Duy Quang"
# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.title())

#Cau3
# s = "Automation Testing"
# subs = s[0:10:1]
# print("Lấy ra từ Automation: ", subs)

# suba = s[11:19:1]
# print("Lấy ra từ Testing: ", suba)

# subb = s[0:5]
# print("Lấy 5 ký tự đầu tiên:" , subb)

# subc = s[15:18]
# print("Lấy 3 ký tự cuối cùng:", subc)

#Cau4
# messy_phone = " 090-123 4567 "
# print(messy_phone.strip())

# new_phone = messy_phone.replace("-","",1)
# print(new_phone.strip())

# new_phone2 = new_phone.replace(" ", "",2)
# print(new_phone2)

#Cau5
#Dùng join() để nối list thành một chuỗi dạng: "apple, banana, cherry".
# fruits = ["apple", "banana", "cherry"]
# print(",".join(fruits))

# #Cau6
# log = "ERROR: Login failed at 10:45"
# bug = "ERROR"
# if bug in log:
#     print("❌ Có lỗi xảy ra")
# else:
#     print("✅ Hệ thống bình thường")



# user_email = "automation.tester01@g-mail.com"
# sub = user_email[0:19]
# print(sub)

title = "Top 5 Laptop Gaming Đáng Mua Nhất"
new = title.lower()
new1 = new.replace(" ", "-" )
print(new1)