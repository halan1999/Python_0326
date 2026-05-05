#1.Tao list gom 5 so va tinh tong tat ca cac so trong list
nums = [1, 2, 3, 4, 5]
print(sum(nums))

#2.Viet chuong trinh in ra tat ca cac phan tu cua dict {"name":"Khoa", "age": 26, "city": "Da Nang"}
infor = {"name":"Khoa", "age": 26, "city": "Da Nang"}
for key, value in infor.items():
    print(key, value)

#3.Khai bao bien sau: a = 10, b = 3.5, c = True, d = None, e = "Python"
#In ra kieu du lieu cua tung bien
a = 10
b = 3.5
c = True
d = None
e = "Python"
print(type(a), type(b), type(c), type(d), type(e))

#Tao list scores = [9, 7, 10, 8, 6]
scores = [9, 7, 10, 8, 6]

#In ra diem cao nhat
print(max(scores))

#Tinh diem trung binh
print(sum(scores)/len(scores))

#Them diem 5 vao cuoi list
scores.append(5)
print(scores)

#Tao tuple birthday = (13, 6, 2000), in ra ngay thang nam
birthday = (13, 6, 2000)
day, month, year = birthday

print("Ngay:", day)
print("Thang:", month)
print("Nam:", year)

# Thử thay đổi tuple (sẽ lỗi)
try:
    birthday[0] = 12
except TypeError as e:
    print("Loi khi thay doi tuple:", e)

#4.Tao dictionary student = {"name": Khoa, "age": 26, "email":"khoa@gmail.com"}
student = {"name":"khoa", "age": 26, "email":"khoa@gmail.com"}
print("Name:", student["name"])
print("Email:", student["email"])

#5. Set emails
emails = {"alice@gmail.com", "bob@gmail.com", "bob@gmail.com"}
print(emails)

# Thêm phần tử
emails.add("ethen@gmail.com")
print(emails)

# remove vs discard
emails.remove("alice@gmail.com") # sẽ lỗi nếu không tồn tại
print(emails)

emails.discard("notexistent@gmail.com")  # không lỗi nếu không tồn tại
print(emails)