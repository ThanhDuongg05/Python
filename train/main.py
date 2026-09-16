# age = 25
# print(age)
# print(type(age))
# price_str="99.99"
# price = float(price_str)
# print(price)
# print(type(price))
# a=7
# b=2
# chia_du=a/b
# chia_nguyen=a//b
# print(chia_du)
# print(chia_nguyen)

email = "  NamNguyen@Gmail.com  "
email = email.strip().lower()
print(email)

full_name="Nguyen Van Nam"
danh_Sach_Tu=full_name.strip().split() 
# Xóa khoảng trắng thừa ở đầu/cuối và tách thành danh sách các từ

ho=danh_Sach_Tu[0]
ten=danh_Sach_Tu[-1]
print(ho,ten)

thong_tin=f"Họ tên: {full_name}, Email: {email}"
print(thong_tin)


fruits = ["apple", "banana", "cherry"]

len(fruits)        # đếm số phần tử → 3
fruits[0]          # lấy phần tử đầu tiên → "apple"
fruits[-1]         # lấy phần tử cuối cùng → "cherry"
fruits.append("mango")   # thêm phần tử vào cuối → ["apple","banana","cherry","mango"]
fruits.remove("banana")  # xóa phần tử theo giá trị

#Duyệt qua list (loop):
for fruit in fruits:
    print(fruit)

#List comprehension 
#(cách viết ngắn gọn, hay dùng trong Data Engineering để transform dữ liệu nhanh):
numbers = [1, 2, 3, 4, 5]
squared = [n**2 for n in numbers]   # [1, 4, 9, 16, 25]

#Lọc dữ liệu trong list:
even_numbers = [n for n in numbers if n % 2 == 0]   # [2, 4]

# bai tap
prices = [100, 250, 75, 300, 50]

for price in prices:
    print(price)

discounted=[price*0.9 for price in prices]

expensive=[price for price in prices if price > 100]

#Dictionary (Từ điển) trong Python
person = {
    "name": "Nam",
    "age": 25,
    "city": "Ho Chi Minh"
}

person["name"]         # lấy giá trị theo key → "Nam"
person["age"] = 26      # cập nhật giá trị
person["job"] = "Data Engineer"   # thêm key mới

#Duyệt qua dictionary:
for key, value in person.items():
    print(key, "-", value)

#Lấy tất cả key hoặc value:
person.keys()     # dict_keys(['name', 'age', 'city', 'job'])
person.values()   # dict_values(['Nam', 26, 'Ho Chi Minh', 'Data Engineer'])

#Kiểm tra key có tồn tại không:
"name" in person   # True
"salary" in person # False

#List chứa nhiều dictionary (rất hay gặp — giống dữ liệu bảng, mỗi dict là 1 dòng):
employees = [
    {"name": "Nam", "salary": 1000},
    {"name": "Lan", "salary": 1200},
    {"name": "Huy", "salary": 900}
]

#Bai tap
product={
    "name":"Laptop",
    "price": 15000000,
    "stock":10
}
print(product["price"])

product["stock"] = 5
for key,value in product.items():
    print(key,"-",value)


employees = [
    {"name": "Nam", "salary": 1000},
    {"name": "Lan", "salary": 1200},
    {"name": "Huy", "salary": 900}
]
for emp in employees:
    print(emp["name"],"co luong",emp["salary"])
