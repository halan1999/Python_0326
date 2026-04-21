#Câu 1
numbers = [1,2,4.5,-5,8]
total = sum(numbers)
print(total)

#Câu 2
info = {"name": "Lan", "age": 25, "city": "Hà Nội"}
for key, value in info.items():
    print(key, value)

#câu 3
a = 10                                                                                                                                                                                                        
b = 3.5                                                                                                                                                                                                        
c = True                                                                                                                                                                                                        
d = None                                                                                                                                                                                                        
e = "Python"
print(type(a), type(b), type(c), type(d), type(e))

scores = [9, 7, 10, 8, 6]
print("Điểm cao nhất:", max(scores))
print("Điểm trung bình:", sum(scores) / len(scores))

scores.append(5)
print(scores)

birthday = (11, 9, 2025)
print("Ngày", birthday[0])
print("Tháng", birthday[1])
print("Năm", birthday[2])


print("Ngày", birthday[0], "Tháng", birthday[1], "Năm", birthday[2])


#Câu 4
student = {"name": "Lan", "age": 18, "email": "lan@gmail.com"}
print(student["name"],student["email"])

#Câu 5
emails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}
emails.add("c@gmail.com")
print(emails)

# delete có báo lỗi khi phần tử không tồn tại
emails.remove("d@gmail.com")
print(emails)

# delete không báo lỗi khi phần tử không tồn tại
emails.discard("d@gmail.com")
print(emails)


