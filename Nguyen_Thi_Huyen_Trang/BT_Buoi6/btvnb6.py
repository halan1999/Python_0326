import openpyxl, json


try:
    wb = openpyxl.load_workbook("data/btvnb6.xlsx")
    sheet = wb.active

    list_student = []
    for row in sheet.iter_rows(min_row = 2, max_col= 4, values_only = True):
        ID, Name, Score, Level = row
        Student = {
            "ID" : ID,
            "Name" : Name,
            "Score" : Score,
            "Level" : Level
            }
        list_student.append(Student)
    with open("data/jsonbt6.json", "w", encoding = 'utf-8') as f:
        json.dump(list_student, f, ensure_ascii=False, indent=4)
    print("Print successfully")

except FileNotFoundError:
    print('Error: Not found file in given path')
except Exception as e:
    print(f"Error: {e}")

