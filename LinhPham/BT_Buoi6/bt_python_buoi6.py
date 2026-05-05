# Bài tập tổng hợp cuối buổi
import json, openpyxl

wb = openpyxl.load_workbook("../BT_Buoi6/students.xlsx")
sheet = wb.active
listsv = []
for row in sheet.iter_rows (min_row=3, values_only=True):
    stt, id, name, score = row
    sv = {
            "ID": id,
            "Tên" : name,
            "Tình trạng" : "Xuất sắc"
        }
    if score >=9:
        listsv.append(sv)
    
with open("../BT_Buoi6/jsfile.json", "w", encoding="utf-8") as file:
    json.dump(listsv, file, ensure_ascii=False, indent=4)
    
