# 1. Tạo 1 list gồm 5 số 
number = [5,10,15,20,25]
print(number)
# 2. Viết chương trình in ra tất cả các phần tử của
# dict {"name": "Lan", "age": 25, "city": "Hà Nội"}.
dict_person ={"name": "Lan", "age": 25, "city": "Hà Nội"}
print(dict_person)
# 3. Khai báo biến sau:                                                                                                                                                                                                        
                                                                                                                                                                                                        
# a = 10                                                                                                                                                                                                        
# b = 3.5                                                                                                                                                                                                        
# c = True                                                                                                                                                                                                        
# d = None                                                                                                                                                                                                        
# e = "Python"                                                                                                                                                                                                        
                                                                                                                                                                                                        
# In ra kiểu dữ liệu của từng biến (type()).    
a = 10                                                                                                                                                                                                        
b = 3.5                                                                                                                                                                                                        
c = True                                                                                                                                                                                                        
d = None                                                                                                                                                                                                        
e = "Python"
print(type(a),type(b),type(c),type(d),type(e))                                                                                                                                                                                                    
                                                                                                                                                                                                        
# Tạo list scores = [9, 7, 10, 8, 6] và làm:                                                                                                                                                                                                        
                                                                                                                                                                                                        
# In ra điểm cao nhất.                                                                                                                                                                                                        
scores = [9, 7, 10, 8, 6] 
print(max(scores))                                                                                                                                                                                                       
# Tính điểm trung bình.                                                                                                                                                                                                        
print(sum(scores) / len(scores))                                                                                                                                                                                                        
# Thêm điểm 5 vào cuối list.                                                                                                                                                                                                        
scores.append(5)   
# print(scores)                                                                                                                                                                                                     
# Tạo tuple birthday = (11, 9, 2025) → in ra ngày, tháng, năm. 
birthday =(11, 9, 2025)  
print (birthday[0], birthday[1], birthday[2])                                                                                                                                                                                                     
# Thử thay đổi giá trị trong tuple và quan sát lỗi.
birthday [0] = 13
print(birthday)
# "4. Tạo dictionary student = {""name"": ""Lan"", ""age"": 18, ""email"": ""lan@gmail.com""}.
student = {"name": "Lan", "age": 18, "email": "lan@gmail.com"}
# In ra tên và email."
print (student ["name"], student ["email"])