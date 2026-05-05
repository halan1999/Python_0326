# Viết chương trình Python để:
# Đọc dữ liệu từ file students.xlsx.
# Lưu dữ liệu vào list of dict trong Python.
# Ghi dữ liệu này ra file report.json theo format JSON, giữ nguyên tiếng Việt.

import openpyxl, json

try:
    wb = openpyxl.load_workbook("../PYTHON/BT_Buoi6/btvn/students1.xlsx")
    sheet = wb.active
    list_data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        id, username, score, rank = row
        score = float(score)
        data = {
            "ID": id,
            "Username": username,
            "Score": score,
            "Rank": rank
        }
        list_data.append(data)
    with open("../PYTHON/BT_Buoi6/btvn/report1.json", "w", encoding='utf-8') as f:
        json.dump(list_data, f, ensure_ascii=False, indent=4)
    
except FileNotFoundError:
    print("File Not Found")
except Exception as e:
    print(f"{e}")