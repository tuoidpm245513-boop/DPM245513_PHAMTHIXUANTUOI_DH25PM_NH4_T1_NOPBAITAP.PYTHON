# Các loại lỗi khi lập trình Python và cách bắt lỗi

# 1. Lỗi cú pháp (Syntax Error)
# Xảy ra khi mã nguồn không tuân thủ cú pháp Python.
# Ví dụ:
# print("Hello"  # Thiếu dấu đóng ngoặc

# 2. Lỗi thực thi (Runtime Error)
# Xảy ra khi chương trình đang chạy, ví dụ chia cho 0, truy cập biến chưa khai báo.
# Ví dụ:
# x = 10 / 0  # ZeroDivisionError

# 3. Lỗi logic (Logic Error)
# Chương trình chạy không báo lỗi nhưng kết quả sai.
# Ví dụ:
# def add(a, b):
#     return a - b  # Lỗi logic: dùng phép trừ thay vì cộng

# Cách bắt lỗi trong Python: sử dụng khối try-except

try:
    x = int(input("Nhập số nguyên: "))
    y = 10 / x
    print("Kết quả:", y)
except ValueError:
    print("Lỗi: Bạn phải nhập số nguyên.")
except ZeroDivisionError:
    print("Lỗi: Không được chia cho 0.")
except Exception as e:
    print("Lỗi khác:", e)
else:
    print("Không có lỗi xảy ra.")
finally:
    print("Kết thúc chương trình.")

# Giải thích:
# - try: Đặt mã có thể gây lỗi vào đây.
# - except: Bắt và xử lý lỗi cụ thể.
# - else: Thực hiện nếu không có lỗi.
# - finally: Luôn thực hiện, dù có lỗi hay không.