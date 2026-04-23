import json
# Bài 1: Nhập số
# Viết chương trình yêu cầu người dùng nhập số.
# Nếu nhập đúng → in bình phương.
# Nếu nhập sai → in "Sai định dạng".

# try:
#     a = int(input("input a: "))
#     print(f"bình phương a: {a**2}")
# except ValueError:
#     print(f"sai định dạng")

# Bài tập 3: Xử lý ValueError và lỗi logic với raise
# Bài toán: Viết một chương trình yêu cầu người dùng nhập vào năm sinh và tính tuổi của họ. Chương trình phải xử lý được các trường hợp nhập sai.

# Yêu cầu:
# Sử dụng khối try-except để bắt lỗi ValueError nếu người dùng nhập vào chữ thay vì số.
# Sau khi chuyển đổi thành số thành công, hãy kiểm tra xem năm sinh có hợp lệ hay không (ví dụ: không được lớn hơn năm hiện tại).
# Nếu năm sinh không hợp lệ, hãy dùng raise ValueError để chủ động tạo ra một lỗi với thông báo ""Năm sinh không thể lớn hơn năm hiện tại.""
# Sử dụng khối else để in ra tuổi của người dùng chỉ khi mọi thứ đều hợp lệ.

# try:
#     year_of_birth = int(input("Year of birth: "))
#     if year_of_birth > 2026:
#         raise ValueError("The year of birth must not be later than 2026")
# except ValueError:
#     print("Please input number!!")
# else:
#     print("Your of birthday is: ", 2026 - year_of_birth)

# bài tập 2
# with open("../BT_Buoi5/data/data.json","r", encoding='utf-8') as f:
#     try:
#         user_data = json.load(f)
#         print("Nội dung data: ", user_data)
        
#     except FileNotFoundError:
#         print("File not found")   
#     finally:
#         print("Kết thúc chương trình")