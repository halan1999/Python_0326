# Bài 1: Nhập số
# Viết chương trình yêu cầu người dùng nhập số.
# Nếu nhập đúng → in bình phương.
# Nếu nhập sai → in "Sai định dạng".
try:
    x = float(input("Nhap gia tri: "))
    print("Binh phuong: ", x ** 2)
except ValueError:
    print("Sai dinh dang")

# Bài 2: File
# Đọc file data.txt.
# Nếu file tồn tại → in nội dung.
# Nếu không → in "File không tồn tại".
# Luôn in "Kết thúc chương trình".
try:
    with open("data.txt", "r", encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print("File does not exit")
finally:
    print("End of program")


# Bài tập 3: Xử lý ValueError và lỗi logic với raise
# Bài toán: Viết một chương trình yêu cầu người dùng nhập vào năm sinh và tính tuổi của họ. Chương trình phải xử lý được các trường hợp nhập sai.
# Yêu cầu:
# Sử dụng khối try-except để bắt lỗi ValueError nếu người dùng nhập vào chữ thay vì số.
# Sau khi chuyển đổi thành số thành công, hãy kiểm tra xem năm sinh có hợp lệ hay không (ví dụ: không được lớn hơn năm hiện tại).
# Nếu năm sinh không hợp lệ, hãy dùng raise ValueError để chủ động tạo ra một lỗi với thông báo "Năm sinh không thể lớn hơn năm hiện tại."
# Sử dụng khối else để in ra tuổi của người dùng chỉ khi mọi thứ đều hợp lệ.
try:
    nam_sinh = int(input("Nhap nam sinh: "))
    nam_hien_tai = 2026
    if(nam_sinh > nam_hien_tai):
        raise ValueError("Nam sinh khong the lon hon nam hien tai.")
except ValueError as e:
    print(e)
else:
    tuoi = nam_hien_tai - nam_sinh
    print("Tuoi cua ban la: ", tuoi)