
# Bài 1: Nhập số
# Viết chương trình yêu cầu người dùng nhập số.
# Nếu nhập đúng → in bình phương.
# Nếu nhập sai → in "Sai định dạng".
try:
    a = int(input("Input number: "))
    print("The square of a is: ", a ** 2)
except ValueError:
    print("Invalid format")

