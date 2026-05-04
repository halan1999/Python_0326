#Bai1
try:
    a = int(input("Input number a: "))
    b = int(input("Input number b: "))
    print(f"number a: {a}, nummber b: {b}")
except Exception as e:
    print(f"Error: {e}")

#Bai 3
try:
    a = int(input("When were you born: "))
    if (a > 2026):
        raise ValueError ("Your birth year can not be greater than the current year")
except Exception as e:
    print(f"Error: {e}")
else:
    print(f"Your age is: {2026-a}")