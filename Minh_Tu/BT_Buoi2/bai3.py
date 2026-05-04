a = 10                                                                                                                                                                                                        
b = 3.5                                                                                                                                                                                                        
c = True                                                                                                                                                                                                        
d = None                                                                                                                                                                                                        
e = "Python"   

print(type(a), type(b), type(c), type(d), type(e))

#tính điểm lớn nhất
scores = [9, 7, 10, 8, 6]
print(max(scores))

#lấy giá trị trung bình
average = sum(scores) / len(scores)
print(average)

#thêm điểm 5 vào cuối list
scores.append(5)
print(scores)

#in ngày tháng năm của tuple và Thử thay đổi giá trị trong tuple và quan sát lỗi.
birthday = (11, 9, 2025)

print('ngày:', birthday[0])
print('tháng:', birthday[1])
print('năm:', birthday[-1])

birthday[1] = 10
print(birthday)

