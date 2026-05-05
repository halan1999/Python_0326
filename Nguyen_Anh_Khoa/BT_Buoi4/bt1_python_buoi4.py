#1.Kiem tra message dang nhap xem co nam trong danh sach sau
expected_message = ["Login successfull", "Welcome"]
actual_message = "Welcome"

if actual_message in expected_message:
    print("Message valid")
else:
    print("Message invalid")

#2.Tim so chia het cho 7 dau tien trong day tu 1 den 100 va in ra man hinh
for i in range(1,101):
    if (i % 7 == 0):
        print(i)
        break

#3.Phan loai hoc luc theo diem trong list sau
scores = [95, 82, 67, 45, 88, 90, 50]
dtb = sum(scores)/len(scores)
print(dtb)
if dtb >= 90:
    print("Xuat sac")
elif dtb >=70:
    print("Kha")
elif dtb >= 50:
    print("Trung binh")
else:
    print("Yeu")