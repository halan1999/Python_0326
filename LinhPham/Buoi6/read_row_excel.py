# How to read a row in excel File
import openpyxl

try:
    wb = openpyxl.load_workbook("D:../Buoi6/example_file.xlsx")
    sheet = wb.active
    for row in sheet.iter_rows(min_row=3, values_only=True):
        stt, username, password, result = row
        print(f"Username: {username}, Passs{password}, Expected result: {result}")
        
except FileNotFoundError:
    print("File not found")
except Exception as mess:
    print(mess)