# #OOP basic
# #OOP (Object-Oriented Programming) giúp bạn đóng gói dữ liệu + hành vi liên quan 
# # vào 1 khối gọi là class. Trong Data Engineering, 
# # bạn không viết OOP nhiều như dân phát triển phần mềm,
# #  nhưng cần hiểu vì hầu hết thư viện bạn dùng (pandas, Spark...) 
# # đều được xây dựng bằng OOP — hiểu OOP giúp bạn đọc hiểu code/document dễ hơn.

# #Định nghĩa class cơ bản:
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def show_info(self):
#         return f"{self.name} có lương {self.salary}"
# #class Employee: — định nghĩa 1 class tên Employee
# #__init__ — hàm khởi tạo (constructor), tự động chạy khi tạo object mới,
# #  dùng để gán giá trị ban đầu
# #self — đại diện cho chính object đó 
# # (bắt buộc phải có ở tham số đầu tiên của mọi method trong class)
# #self.name, self.salary — gọi là attribute (thuộc tính), 
# # lưu dữ liệu của object

# #Tạo object (instance) từ class:
# emp1 = Employee("Nam", 1000)
# emp2 = Employee("Lan", 1200)

# print(emp1.name)         # "Nam"
# print(emp1.show_info())  # "Nam có lương 1000"
# print(emp2.show_info())  # "Lan có lương 1200"
# #emp1, emp2 là 2 object (instance) khác nhau, 
# # được tạo từ cùng 1 class Employee, nhưng có dữ liệu riêng.

# #Thêm method để thay đổi dữ liệu:
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def show_info(self):
#         return f"{self.name} có lương {self.salary}"

#     def raise_salary(self, amount):
#         self.salary += amount

# emp1 = Employee("Nam", 1000)
# emp1.raise_salary(200)
# print(emp1.show_info())   # "Nam có lương 1200"

# # Cách dùng dict (như bài trước) — dữ liệu và hành vi tách rời
# emp_dict = {"name": "Nam", "salary": 1000}

# # Cách dùng class — dữ liệu và hành vi gộp lại, có thể gọi method trực tiếp
# emp_obj = Employee("Nam", 1000)
# emp_obj.raise_salary(200)

#BAI TAP
#cau 1:
class Product:
    def __init__ (self,name,price):
        self.name=name
        self.price=price

    def show_info(self):
            return f"{self.name} có gia {self.price}"

    
p1 = Product("Laptop", 15000000)

print(p1.name)        
print(p1.show_info())

#cau 2:
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def show_info(self):
        return f"{self.name} có gia {self.price}"
    def apply_discount(self,percent):
        self.price = self.price * (1 - percent/100)

p2 = Product("Mouse", 200000)
p2.apply_discount(10)
print(p2.show_info())

