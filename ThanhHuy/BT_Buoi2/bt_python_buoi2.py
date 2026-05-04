#Bai1
listSum = [1, 2, 3, 4, 5]
print(f"Tong cua listSum: {sum(listSum)}")

# #Bai2
info = {"name": "Lan", "age": 25, "city": "Hà Nội"}
print(info)

# #Bai3
a = 10                                                                                                                                                                                                        
b = 3.5                                                                                                                                                                                                        
c = True                                                                                                                                                                                                        
d = None                                                                                                                                                                                                        
e = "Python" 
print(type(a), type(b), type(c), type(d), type(e))

listScore = [9, 7, 10, 8, 6]

print(f"Highest score: {max(listScore)}")

dtb = sum(listScore)/len(listScore)
print(f"Average score: {dtb}")

listScore.append(5)
print(f"The list afer updated: {listScore}")

birthdayTuple =  (11, 9, 2025)
print(birthdayTuple)
print(birthdayTuple[0])
#birthdayTuple[0] = 11 TypeError: 'tuple' object does not support item assignment

# #Bai4
student = {"name": "Lan", "age": 18, "email": "lan@gmail.com"}
print(f"Ten la: {student["name"]}, dia chi email: {student["email"]}")

#Bai5
emails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}
emails.add("c@gmail.com")
emails.remove("d@gamil.com")
#emails.discard("d@gmail.com")
# nếu xoá phần tử ko tồn tại thì remove báo lỗi còn discard thì không báo lỗi