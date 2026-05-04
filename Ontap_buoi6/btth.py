import openpyxl
import json

try:
    workbook = openpyxl.load_workbook("btth.xlsx")
    sheet = workbook.active 
    verygood_students = []
    good_students = []
    for row in sheet.iter_rows(min_row=2,max_col=3, values_only=True):
        id, name, score = row
        score = float(score)
        if score >= 9:                  
            student_data = {
            "ID": id,
            "Họ tên": name,
            "Điểm": score
        }
            verygood_students.append(student_data)  
        elif 7 <= score < 9:
            student_data = {
            "ID": id,
            "Họ tên": name,
            "Điểm": score
        }
            good_students.append(student_data)    
    with open("verygood.json", "w", encoding="utf-8") as json_file:
        json.dump({"verygood": verygood_students}, json_file, indent=4, ensure_ascii=False)
    with open("good.json", "w", encoding="utf-8") as json_file:
        json.dump({"good": good_students}, json_file, indent=4, ensure_ascii=False)
    print("Đã lưu dữ liệu thành công vào file verygood.json và good.json!")
except FileNotFoundError:
    print("Lỗi: Không tìm thấy file btth.xlsx. Bạn hãy kiểm tra lại tên file nhé.")
except Exception as e:
    print(f"Đã xảy ra lỗi ngoài ý muốn: {e}")
finally:
    print("Chương trình đã kết thúc.")