import openpyxl,json

wb = openpyxl.load_workbook("../BT_Buoi6/data/bt6.xlsx")

sheet = wb.active
try:
    list_student =[]

    for row in sheet.iter_rows(min_row = 2, values_only=True):
        id, name, score, rank = row
        student ={
            "ID":id,
            "Họ tên":name,
            "Điểm":score,
            "Xếp hạng":rank
        }
        list_student.append(student)
        print(student)
    with open("../BT_Buoi6/data/Liu.json","w", encoding='utf-8') as f:
        json.dump(list_student, f, ensure_ascii=False, indent=4)
except FileNotFoundError:
    print("File not found")
except Exception as e:
    print(e)

