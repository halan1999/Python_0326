try:
    print(5/0)
except ZeroDivisionError:
    print("Lỗi chia cho 0")
finally:
    print("Kết thúc")
