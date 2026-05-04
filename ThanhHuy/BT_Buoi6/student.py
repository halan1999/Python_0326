import openpyxl, json

wb = openpyxl.load_workbook("./buoi6/data/student.xlsx")
sheet = wb.active

verygood_student = []

for row in sheet.iter_rows(min_row=3, values_only=True):
    stt, id, name, score = row
    if(float(score) >= 9):
        verygood_student.append({
            "ID": id,
            "Name" : name,
            "Level" : "Very good"
        })

with open("./buoi6/data/report.json", "w", encoding='utf-8') as f:
    json.dump(verygood_student, f, ensure_ascii = False, indent = 2)
print("Completed write Json file")