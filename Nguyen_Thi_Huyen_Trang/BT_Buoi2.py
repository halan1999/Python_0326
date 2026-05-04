# 1.Tạo list gồm 5 số, tính tổng tất cả các số trong list.
a = [1,2,3,4,5]
print(sum(a))

2. # Viết chương trình in ra tất cả các phần tử của dict {"name": "Lan", "age": 25, "city": "Hà Nội"}.
b = {"name": "Lan", "age": 25, "city": "Hà Nội"}
print(b)

3. #Khai báo biến sau: 
a = 10
b = 3.5
c = True  
d = None 
e = "Python"   

# In ra kiểu dữ liệu của từng biến (type()). 
print(type(a), type(b), type(c), type(d), type(e))

#Tạo list scores = [9, 7, 10, 8, 6] và làm: 
scores = [9, 7, 10, 8, 6]

#In ra điểm cao nhất.
print(max(scores))  

#Tính điểm trung bình
ave = sum(scores) /len(scores)
print(ave)

#Thêm điểm 5 vào cuối list. 
scores.append(5)
print(scores)  

#Tạo tuple birthday = (11, 9, 2025) → in ra ngày, tháng  năm.   
bth = (11, 9, 2025) 
print("Ngày:", bth[0])
print("Tháng:", bth[1])
print("Năm:", bth[2])

# Thử thay đổi giá trị trong tuple và quan sát lỗi. 
bth[0]= 2025
print(bth)
#không thay đổi được

#4. Tạo dictionary student = {"name": "Lan", "age": 18, "email": "lan@gmail.com"}.
#In ra tên và email.
dic = {"name": "Lan", "age": 18, "email": "lan@gmail.com"}
print(dic["name"], dic["email"])

#5. Tạo set emails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}.
#Quan sát kết quả khi in set ra.
set = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}
print(set)
#Set chỉ in ra 1 value nếu có 2 value giống nhau

#Thêm "c@gmail.com".
set.add("c@gmail.com")
print(set)

#Thử xóa "d@gmail.com" bằng remove và bằng discard, giải thích sự khác nhau.
set.add("d@gmail.com")
#set.remove("d@gmail.com")
set.discard("d@gmail.com")
#Không giống như set.remove(), phương thức discard() sẽ không gây ra lỗi (exception) khi phần tử không tồn tại trong tập hợp

