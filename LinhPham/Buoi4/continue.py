# Countinue dùng trong vòng lặp để bỏ qua khi thỏa yêu cầu

numbers = [1,2,3,4,5,6,7,8,9,10]
for so in numbers:
    if (so % 2 ==0):
        continue
    print(so)

# Giải thích thêm vòng lặp này chạy qua tất cả cá số và số nào chia hết cho 2 thì bỏ qua