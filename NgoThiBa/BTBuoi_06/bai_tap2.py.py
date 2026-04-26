import openpyxl, json

try:
    wb = openpyxl.load_workbook("C:/PYTHON/BT_Buoi6/students.xlsx")
    sheet = wb.active
    
    list_student = []
    for row in sheet.iter_rows(min_row=3,max_row= 6,values_only=True):
        stt, id, name, score = row [:4]
        score = float(score)
        if score >= 9:
            student = {
                "ID": id,
                "Tên": name,
                "Tình trạng": "Học lực giỏi"
            }      
            list_student.append(student)
    
    with open("C:/PYTHON/report.json","w",encoding="utf-8") as f:
        json.dump(list_student, f, ensure_ascii= False, indent= 4)
except FileExistsError:
    print("File student is not exsiting")
except Exception as e:
    print(e)
