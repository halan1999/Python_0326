# Câu 1: Nhập số
try:
    a = int(input("Please enter a number: "))
    print(a)
except ValueError as mess:
    print("Error: ", mess)
    

# Câu 3:
try:
    yob = int(input("Please enter your YOB: "))
    if yob > 2026:
        raise ValueError ("YOB should less than 2026")
    elif yob < 1700:
        raise ValueError ("Are you superman?")
except ValueError as text:
    print("Erorr: ", text)
else:
    print ("Your age is: ", 2026 - yob)