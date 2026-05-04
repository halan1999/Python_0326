import openpyxl, json

wb = openpyxl.load_workbook("./buoi6/data/btvn.xlsx")
sheet = wb.active

students = []

for row in sheet.iter_rows(min_row=2, values_only=True):
    id, name, score, level = row
    students_list = {
        "ID": id,
        "Name" : name,
        "Score" : score,
        "Level" : level
    }
    students.append(students_list)
with open("./buoi6/data/btvn.json", "w", encoding='utf-8') as f:
    json.dump(students, f, ensure_ascii = False, indent = 2)
print("Completed write Json file")