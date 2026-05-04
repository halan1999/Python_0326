import openpyxl
import json

try:
    workbook = openpyxl.load_workbook("../Buoi6/students.xlsx")
    sheet = workbook.active 
    student_list = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        student_data = {
            "ID": row[0],
            "Họ tên": row[1],
            "Điểm": row[2],
            "Xếp loại": row[3]
        }
        student_list.append(student_data)
    with open("../Buoi6/report.json", "w", encoding="utf-8") as json_file:
        json.dump(student_list, json_file, indent=4, ensure_ascii=False)
    print("Đã lưu dữ liệu thành công vào file report.json!")
except FileNotFoundError:
    print("Lỗi: Không tìm thấy file students.xlsx. Bạn hãy kiểm tra lại tên file nhé.")
except Exception as e:
    print(f"Đã xảy ra lỗi ngoài ý muốn: {e}")