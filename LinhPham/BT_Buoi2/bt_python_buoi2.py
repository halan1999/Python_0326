# Câu 1: Tính tổng các số trong list
list_so = [1, 2, 3, 4, 5]
print (sum(list_so))

# Câu 2: In các phần tủ
infor = {"name": "Lan", "age": 25, "city": "HaNoi"}
for value in infor.values(): print(value)

# Câu 3
a = 10
b = 3.5
c = True
d = None
e = "Python"
# In kiểu dữ liệu của từng biến
print (type(a), type(b), type(c), type(d), type(e))

scores = [9, 7, 10, 8, 6]
# In điểm cáo nhất
print(max(scores))

# Tinh diem trung binh
DiemTrungBinh = (sum(scores)/len(scores))

# Them diem 5 vao cuoi list
scores.insert(6, 5.1)
scores.append(5.2)

birthDay = (11, 9, 2005)
# In ra ngay thang name
print (birthDay)

#Cau 4: In tên và email
student = {"name": "Lan", "age": 18, "email": "lan@gmail.com"}
print(student ["name"], student["email"])


