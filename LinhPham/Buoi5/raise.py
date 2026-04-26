# Raise là công cụ để dừng chương trình tại thời điểm mà ta thấy được nó đã bị sai logic, và raise cũng chính là công cụ đặt ra logic
# Raise tự định nghĩa lỗi, không cần dùng lỗi có sẵn của Python trong exception


try:
    a = int(input("Please enter a value: "))
    b = int(input("Please enter b value: "))
    if (b == a):
        raise ValueError ("b cannot equal a")
    elif (b<0):
        raise ValueError ("b cannot less than 0")
except Exception as ErrorMess:
    print("Error:", ErrorMess)
else: #Hàm else này KHÔNG lquan gì đến if ở trên, và hàm else này sẽ chỉ chạy khi tất cả các khối lệnh trong try không có Lỗi Exception nào
    print("Successfully") 
finally:
    print ("Test pass")