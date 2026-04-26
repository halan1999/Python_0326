# How to read a cell in excel file
import openpyxl

# Cách lấy 1 ô

try:
    wb = openpyxl.load_workbook("../Buoi6/example_file.xlsx")
    sheet1 = wb.active # này là mặc định lấy sheet đầu tiên
    cell1 = sheet1["B3"].value
    print ("The B3 cell value is: ", cell1)
except FileNotFoundError:
    print (" File not found")
except Exception as mess:
    print(mess)