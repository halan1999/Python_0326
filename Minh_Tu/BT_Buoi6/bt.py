import openpyxl
import json

students = []

#Lưu dữ liệu vào list of dict trong Python.
try:
    wb = openpyxl.load_workbook('../python/BT_Buoi6/students.xlsx')
    sheet = wb.active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        ID, username, grade, rank = row
        student = {
            "ID": ID,
            "Username": username,
            "Grade": grade,
            "Rank": rank
        }
        students.append(student)
        print(students)
    
    #Ghi dữ liệu này ra file report.json theo format JSON, giữ nguyên tiếng Việt.     
    with open('../python/BT_Buoi6/report.json', 'w', encoding='utf-8') as f:
        json.dump(students, f, ensure_ascii=False, indent=4)

    print("Đã ghi file report.json thành công")
    
except FileNotFoundError:
    print('File not found')
except Exception as e:
    print(e)


    
