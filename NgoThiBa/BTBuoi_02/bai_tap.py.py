# #1. Tạo list gồm 5 số, tính tổng tất cả các số trong list.
# list = (1,2,3,-6,10.5)
# #print ("Tổng các số: ", sum(list))

# #2. Viết chương trình in ra tất cả các phần tử.
# dict= {"name": "Lan", "age": 25, "city": "Hà Nội"}
# #print (dict["name"], dict["age"], dict["city"])
                                                                                                                                                                                                                                                                                                                                                                                                           
# #3.List 					
# a = 10                                                                                                                                                                                                        
# b = 3.5                                                                                                                                                                                                        
# c = True                                                                                                                                                                                                        
# d = None                                                                                                                                                                                                        
# e = "Python"
# #print(type(a), type(b), type(c), type(d), type(e))  # In ra kiểu dữ liệu của từng biến (type()). 

# scores = [9, 7, 10, 8, 6]
# #print("Diem cao nhat la: ", max(scores)) # In ra điểm cao nhất. 
# #print("Diem trung binh la: ", sum(scores)/len(scores))  # Tính điểm trung bình.
# scores.append(5)  # Thêm điểm 5 vào cuối list.   
# #print(scores)

# birthday = (11, 9, 2025)
# day = birthday[0]
# month = birthday[1]
# year = birthday[2]
# #print("Ngay sinh la: ", birthday[0], birthday[1], birthday[2])  # Tạo tuple  → in ra ngày, tháng, năm. 

# #4. Dictionary
# student = {"name": "Lan", "age": 18, "email": "lan@gmail.com"}
# #print(student["name"], student["email"])   #In ra tên và email.

# #5. Set
# emails = {"a@gmail.com", "b@gmail.com", "a@gmail.com"}
# #print(emails)  # Quan sát kết quả khi in set ra: email a@gmail.com is duplicated in two positions, so when printed, there are only two values: a@gmail.com and b@gmail.com

# emails.add("c@gmail.com")
# #print(emails)  # Thêm "c@gmail.com"

# # Thử xóa ""d@gmail.com"" bằng remove và bằng discard, giải thích sự khác nhau."
# #emails.remove("d@gmail.com")
# #print(emails) #KeyError: 'd@gmail.com'
# emails.discard("d@gmail.com")
# #print(emails) #no error log, print successfully



emails = {"1@gmail.com", "2@gmail.com"}
emails.add("3@gmail.com")
#print(emails)

#emails.remove("4@gmail.com")
#print(emails)

emails.discard("4@gmail.com")
print(emails)

