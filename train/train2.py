# def greet(name):
#     return f"Xin chào, {name}!"

# result = greet("Nam")
# print(result)   # "Xin chào, Nam!"

# #Hàm có nhiều tham số:
# def calculate_total(price, quantity):
#     return price * quantity

# total = calculate_total(100, 3)
# print(total)   # 300

# #Tham số có giá trị mặc định (default value):
# def apply_discount(price, discount=0.1):
#     return price * (1 - discount)

# print(apply_discount(100))        # 90.0 (dùng discount mặc định 0.1)
# print(apply_discount(100, 0.2))   # 80.0 (ghi đè discount = 0.2)


# #Hàm kết hợp với list (rất hay dùng khi xử lý dữ liệu):
# def double(n):
#     return n * 2

# numbers = [1, 2, 3]
# result = [double(n) for n in numbers]   # [2, 4, 6]


#tinh dien tich hinh chu nhat
# def calculate_area(length ,width) :
#     return length*width
# print (calculate_area(5,3))

# #ham tinh gia sau thue
# def apply_tax(price, tax_rate=0.1):
#     return price+(price*tax_rate)
# print (apply_tax(100))
# print(apply_tax(100,0.2))

# #tra ve gia da cong them 10% thue
# def add_tax(price):
#     return price+ (price*0.1)
# prices = [100,200,300]
# prices_with_tax=[add_tax(price) for price in prices]
# print(prices_with_tax)

#Trong thực tế, dữ liệu thường "bẩn" — có thể thiếu, sai định dạng,
# hoặc gây lỗi khi xử lý. 
# Nếu không xử lý lỗi, chương trình sẽ dừng đột ngột khi gặp lỗi.try/except 
# giúp "bắt" lỗi 
# và xử lý nó mà không làm crash chương trình.
# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Lỗi: không thể chia cho 0")

# #Ví dụ thực tế trong Data Engineering — dữ liệu bị sai kiểu:
# data = "abc"
# try:
#     number = int(data)
# except ValueError:
#     print(f"Không thể chuyển '{data}' thành số")

# #Bắt lỗi chung (không cần biết chính xác loại lỗi):
# try:
#     # code có thể lỗi
#     pass
# except Exception as e:
#     print(f"Có lỗi xảy ra: {e}")

# #Kết hợp try/except với vòng lặp (rất hay dùng khi xử lý nhiều dòng dữ liệu, 
# # có dòng lỗi vẫn tiếp tục xử lý dòng khác):
# values = ["10", "20", "abc", "30"]
# results = []

# for v in values:
#     try:
#         results.append(int(v))
#     except ValueError:
#         print(f"Bỏ qua giá trị lỗi: {v}")

# print(results)   # [10, 20, 30]

#chuyen 100 thanh so nguyen int in ra ko the chuyen doi
num_str = "100"
try:
    number = int(num_str)
    print(number)
except ValueError:
    print("Không thể chuyển đổi")

#Từ list data = ["50", "abc", "75", "xyz", "100"], dùng vòng lặp + try/except 
# để lọc ra các giá trị chuyển được thành số, bỏ qua giá trị lỗi,
#  lưu vào valid_numbers.
data = ["50", "abc", "75", "xyz", "100"]
results=[]
for v in data:
    try:
        results.append(int(v))
    except ValueError:
        print(f"Bo qua gia tri loi {v}")
print(results)