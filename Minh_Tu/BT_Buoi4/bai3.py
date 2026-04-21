scores =[95, 82, 67, 45, 88, 90, 50]
diem_tb = sum(scores)/len(scores)
print(diem_tb)

#hoc sinh xuat sac
if diem_tb >= 90:
    print("hoc sinh xuat sac")
#hoc sinh kha
elif diem_tb >= 70:
    print("hoc sinh kha")
#hoc sinh trung binh
elif diem_tb >= 50:
    print("hoc sinh trung binh")
#hoc sinh yeu
else:
    print("hoc sinh yeu")
    

