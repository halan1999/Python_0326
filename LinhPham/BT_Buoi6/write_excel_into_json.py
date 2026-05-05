# How write the except value into json file
import openpyxl, json

wb = openpyxl.load_workbook("D:../Buoi6/example_file.xlsx")
sheet = wb.active
list_data = []
for row in sheet.iter_rows(min_row=2, values_only=True):
    stt, username, password, result = row
    data = {
        "User name": username,
        "Pass" : password,
        "Expect reuslt" : result
    }
    list_data.append(data) # Câu lệnh thêm dữ liêu của "data" và "list_data"
    
with open ("../Buoi6/write_date_from_excel_file.json", "w", encoding="utf-8") as wf:
    json.dump(list_data, wf, ensure_ascii=False, indent=4)
    
#  json.dump là câu lệnh để thêm thê dự liệu từ "list_data" và "wf"
# ensure_ascii nghĩa là giữ format tiếng viêt
# indent đơn giả là sô lần cách để canh lề thôi
