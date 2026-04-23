# Break dùng để dùng vòng lặp ngay khi đã tìm ra điều kiện đáp ưng
numbers = [1,2,3,4,5,6,8,9,10]
for so in numbers:
    print(so)
    if (so % 2 == 0):
        print("done")
        break

    # Giải thích thêm vòng lặp này chạy qua tất cả cá số và có điều kiện là nếu tìm được số nào chia hết cho 2 thì dừng lại