#1.
expected_messages = ["Login successful", "Welcome"]
actual_message = "Welcome"
if actual_message in expected_messages:
    print("Message valid")
else:
    print("Message invalid")
#2
for i in range (1,101):
    if i % 7 == 0:
        print(i)
        break

#3
scores =[95, 82, 67, 45, 88, 90, 50]
for score in scores:
    if score >= 90:
        print("Xuất sắc")
    elif score >= 70:
        print("Khá")
    elif score >= 50:
        print("Trung bình")
    else:
        print("Yếu")
#4 
for i in range (2,4):
    print(f"Bảng cửu chương {i}:")
    for j in range (1,11):
        print(f"{i} x {j} = {i*j}")