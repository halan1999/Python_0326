import openpyxl
import json

excellentStudents = []
veryGoodAndGoodStudents = []

#Lưu dữ liệu vào list of dict trong Python.
try:
    wb = openpyxl.load_workbook('../python/BT_Buoi6/student_bt_tong_hop.xlsx')
    sheet = wb.active
    for student in sheet.iter_rows(min_row=3, values_only=True):
        stt, ID, username, score = student
        
        #Lấy sinh viên "Xuất sắc" (điểm >= 9)
        if float(score) >= 9:          
            student = {
                "ID": ID,
                "Username": username,
                "Score": score,
            }
            excellentStudents.append(student)
        elif float(score) >=7 and float(score) <9:          
            student = {
                "ID": ID,
                "Username": username,
                "Score": score,
            }
            veryGoodAndGoodStudents.append(student)
    print(excellentStudents)
    print(veryGoodAndGoodStudents)
    
    #Ghi dữ liệu này ra file tong_hop_hs_xuat_sac.json theo format JSON, giữ nguyên tiếng Việt.     
    with open('../python/BT_Buoi6/tong_hop_hs_xuat_sac.json', 'w', encoding='utf-8') as f:
        json.dump(excellentStudents, f, ensure_ascii=False, indent=4)
    
    #Ghi dữ liệu này ra file tong_hop_hs_gioi_va_kha.json theo format JSON, giữ nguyên tiếng Việt.     
    with open('../python/BT_Buoi6/tong_hop_hs_gioi_va_kha.json', 'w', encoding='utf-8') as f:
        json.dump(veryGoodAndGoodStudents, f, ensure_ascii=False, indent=4)
    
except FileNotFoundError:
    print('File not found')
  
except Exception as e:
    print(e)

finally:
    print("Đã ghi json files thành công")