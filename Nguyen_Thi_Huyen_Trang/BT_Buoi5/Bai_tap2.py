# Bài 2: File
# Đọc file data.txt.
# Nếu file tồn tại → in nội dung.
# Nếu không → in "File không tồn tại".
# Luôn in "Kết thúc chương trình".
try:
    with open ("BT_Buoi5/data.txt",'r', encoding = 'utf-8') as f:
        content = f.read()
        print(content)

except FileNotFoundError:
    print("File doesn't exist")
finally:
    print("Finish program")