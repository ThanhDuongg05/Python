# #Lý thuyết
# #Đây là kỹ năng cực kỳ thực tế — 
# # Data Engineer làm việc với file dữ liệu hàng ngày 
# # (CSV, JSON là 2 định dạng phổ biến nhất).

# #1. Đọc/ghi file text cơ bản:
# # Ghi file
# with open("data.txt", "w") as f:
#     f.write("Hello Data Engineer")

# # Đọc file
# with open("data.txt", "r") as f:
#     content = f.read()
#     print(content)

# #with open(...) as f: — cách chuẩn để mở file,
# # tự động đóng file sau khi dùng xong (tránh rò rỉ tài nguyên)
# #"w" = write(ghi, ghi đè nếu file đã tồn tại)
# #"r" = read (đọc)

# #Làm việc với CSV (dùng thư viện csv)
# import csv

# # Ghi file CSV
# with open("employees.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["name", "salary"])   # dòng header
#     writer.writerow(["Nam", 1000])
#     writer.writerow(["Lan", 1200])

# # Đọc file CSV
# with open("employees.csv", "r") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
# #Đọc CSV dạng Dictionary (tiện hơn, hay dùng hơn):
# with open("employees.csv", "r") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(row["name"], "-", row["salary"])


# #Làm việc với JSON (dùng thư viện json) 
# # — cực kỳ quan trọng vì API thường trả JSON:
# import json

# data = {"name": "Nam", "age": 25, "skills": ["Python", "SQL"]}

# # Ghi JSON ra file
# with open("data.json", "w") as f:
#     json.dump(data, f)

# # Đọc JSON từ file
# with open("data.json", "r") as f:
#     loaded_data = json.load(f)
#     print(loaded_data)
#     print(loaded_data["name"])   # "Nam"

#json.dump(obj, file) — ghi object Python (dict/list) ra file JSON
#json.load(file) — đọc file JSON, chuyển thành object Python (dict/list)
#json.dumps(obj) — chuyển object Python thành chuỗi JSON (không ghi file)
#json.loads(string) — chuyển chuỗi JSON thành object Python


#BAI TAP
#Cau1:
import json
employee = {
    "name" : "Huy",
    "salary" : 900,
    "department": "Engineering"
}
#write
with open("employee.json","w") as f:
    json.dump(employee,f)

#Cau 2:
#read
with open("employee.json","r") as f:
    loaded_employee = json.load(f)
    print(loaded_employee)
    print(loaded_employee["salary"])

#cau3:
import csv
with open("product.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["product", "price"])
    writer.writerow(["Laptop", 15000000])
    writer.writerow(["Mouse", 200000])
    writer.writerow(["Keyboard",500000])
#doc file
with open("product.csv","r") as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)
with open("product.csv","r") as f:
    reader=csv.DictReader(f)
    for row in reader:
        print(row["product"]+" gia "+row["price"])