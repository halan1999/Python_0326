numbers = [1, 2.2, -3, 4]
info = ["Linh", 18, "1/1/2000", "Tp DN", "linh@gmail.com"]
empty = []

# Truy cap phan tu
# print(numbers[2])

# Update
numbers [1] = 9
#print(numbers)

numbers [-1] = 3.14
#print (numbers)

fruits = ["Mango", "Melon", "coconut", "kiwi", "peach", "lemon"]
# Add
#fruits.append("banana")
#fruits.insert (2, "apple")
fruits.insert (2, "Berry")


#Xóa dựa vào text
fruits.remove("Mango")

#Xoa Chỉ định thứ tự
fruits.pop(-1)

#Kiem tra so luong phan tu
print (len(fruits))