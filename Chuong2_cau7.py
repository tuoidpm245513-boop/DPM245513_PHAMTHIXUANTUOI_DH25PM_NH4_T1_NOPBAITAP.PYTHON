# Một số cách nhập dữ liệu từ bàn phím trong Python

# 1. Nhập một chuỗi
name = input("Nhập tên của bạn: ")
print("Tên bạn vừa nhập là:", name)

# 2. Nhập một số nguyên
age = int(input("Nhập tuổi của bạn: "))
print("Tuổi bạn vừa nhập là:", age)

# 3. Nhập một số thực
height = float(input("Nhập chiều cao của bạn (m): "))
print("Chiều cao bạn vừa nhập là:", height)

# 4. Nhập nhiều giá trị trên một dòng, phân tách bằng dấu cách
a, b = input("Nhập hai số, cách nhau bởi dấu cách: ").split()
print("Số thứ nhất:", a)
print("Số thứ hai:", b)

# 5. Nhập nhiều số và chuyển sang kiểu số nguyên
numbers = list(map(int, input("Nhập các số nguyên, cách nhau bởi dấu cách: ").split()))
print("Danh sách các số nguyên vừa nhập:", numbers)