#Bài tập 1:
expected_messages = ["Login succesfull", "Welcome"]     
actual_message = "Welcome"

if actual_message in expected_messages:
    print("Message valid")
else:
    print("Message invalid")

#Bài tập 2:
for i in range (1,100):
    if i % 7 == 0:
     print(i)

#Bài tập 3: 
scores = {95, 82, 67, 45, 88, 90, 50}
sum = sum(scores)/len(scores)
print(sum)

if sum >= 90: 
    print("Xuat sac")
elif sum >= 70:
    print("Kha")
elif sum >= 50:
    print("Trung binh")
else:
    print("Yeu")

#Bài tập 4: In ra bảng cửu chương 2, 3
for i in range (1, 11):
    print(f"2 x {i} = ", i * 2) 
    
for a in range (1, 11):
     print(f"3 x {a} = ", a * 3)
    
#Bài tập chung:
products = ["iPhone 13", "Samsung Galaxy", "MacBook Pro 16 inch", "Oppo Reno"]
item = "MacBook Pro 16 inch"
for item in products:
    if "MacBook Pro 16 inch" in products:
        print("Đã tìm thấy sản phẩm")
    break
else:
    print("Không tìm thấy sản phẩm")



numbers = [2, 5, 8, 11, 14, 17, 20]
for i in numbers: #In ra tất cả các số trong list
    print(i)

for a in numbers:   #In ra số chẵn trong list.
    if a % 2 == 0:
        print(a)
        
b = sum(numbers)   #Tính tổng tất cả số trong list.


for i in numbers: #In ra bảng cửu chương của từng số trong list
    print("Bang cuu chuong:",i)
    for f in range (1, 11):
        print(f" {f} x {i}= ", f*i)