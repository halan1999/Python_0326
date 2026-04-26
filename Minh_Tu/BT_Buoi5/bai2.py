try:
    with open('data.txt', 'r') as file:
        print(file.read)
except:
    print('File không tồn tại')
finally:
    print('Kết thúc chương trình')
    
        