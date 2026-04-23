# Câu lệnh try - except trong python được dùng để cho phép khi chạy lỗi vẫn có thể tiếp tục

try:
    yourage = int(input("please enter your age: "))
    if yourage > 0:
        print("your age is: ", yourage)
    else:
        print("your aghe should greater than 0")

except ValueError:
    print("Please enter correct value", ValueError)

print("You can see now, although it gets error, the code still runs")