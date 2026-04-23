import openpyxl
import json

try:
    wb = openpyxl.load_workbook("C:/PYTHON/BT_Buoi6/student.xlsx")
    sheet = wb.active
    list_data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        id, hovaten, diem, xeploai = row
        # print(f"ID: {id}, Họ và tên: {hovaten}, Điểm: {diem}, Xếp loại: {xeploai}")
        
        data = {
            "ID": id,
            "Họ và tên": hovaten,
            "Điểm": diem,
            "Xếp loại": xeploai     
        }
        list_data.append(data)

    with open("C:/PYTHON/data_report.json","w",encoding="utf-8") as f: 
        json.dump(list_data, f, ensure_ascii =False, indent =4)
        
except FileNotFoundError:
    print("File is not existing")
except Exception as e:
    print(e)