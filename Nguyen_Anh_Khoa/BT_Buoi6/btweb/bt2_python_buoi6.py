# Bạn được giao một file Excel students.xlsx chứa danh sách sinh viên và điểm số. Bạn cần viết một chương trình để đọc file này và tạo ra một file report.json cho những sinh viên "Xuất sắc" (điểm >= 9).
import openpyxl, json

try:    
    wb = openpyxl.load_workbook('../PYTHON/BT_Buoi6/btweb/students2.xlsx')
    sheet = wb.active
    list_data = []
    for row in sheet.iter_rows(min_row=3, values_only=True):
        stt, id, name, score = row
        if score is None:
            continue
        score = float(score)
        if (score >= 9):
            data = {
                "STT": stt,
                "ID": id,
                "Name": name,
                "Score": score
            }
            list_data.append(data)

    with open('../PYTHON/BT_Buoi6/btweb/report2.json', 'w', encoding='utf-8') as json_file:
        json.dump(list_data, json_file, ensure_ascii=False, indent=4)

except FileNotFoundError:
    print("The file 'students2.xlsx' was not found.")
except Exception as e:
    print(f"{e}")