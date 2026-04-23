#Set
numbers = {1, 2, 3, 4, 5, 1, 2, 3 ,4 }
print (numbers)


email = {"a@gmail.com", "b@gmail.com", "c@gmail.com", "a@gmail.com"}
# Add new value
email.add ("d@gmail.com")

# Remove a value, nhưng nếu xóa phần tử không tồn tại sẽ báo lỗi
email.remove ("c@gmail.com")

# Remove a value,  xóa phần tử không tồn tại sẽ không báo lỗi
email.discard ("z@gmail.com")
print(email)

#List

emails = ["a@gmail.com", "b@gmail.com", "c@gmail.com", "a@gmail.com"]
print (set(emails))


A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)   # Hợp: {1, 2, 3, 4, 5, 6}
print(A & B)   # Giao: {3, 4}
print(A - B)   # Hiệu: {1, 2}
print(A ^ B)   # Phần tử chỉ có ở 1 tập hợp: {1, 2, 5, 6}
