import pandas as pd
#Bai 4 Group by va thong ke
# df.groupby("department")["salary"].mean() # trung bình theo nhóm
# df.groupby("department")["salary"].sum()     # tổng theo nhóm
# df.groupby("department")["salary"].count()   # đếm số lượng theo nhóm

# #nhieu phep tinh cung luc:
# df.groupby("department")["salary"].agg(["mean","sum","count"])

#BAI TAP
data = {
    "category": ["Electronics", "Electronics", "Food", "Food", "Electronics", "Food"],
    "product": ["Laptop", "Mouse", "Rice", "Milk", "Keyboard", "Bread"],
    "price": [15000000, 200000, 50000, 30000, 500000, 20000],
    "quantity": [2, 10, 100, 50, 15, 80]
}
#bai 1 tinh tong
df=pd.DataFrame(data)
print(df.groupby("category")["price"].sum())

#bai 2 tinh tong san pham(count) trong moi category
print(df.groupby("category")["quantity"].count())

#bai 3: Dùng .agg() để tính cùng lúc 
# mean, sum, max của cột price theo từng category.
print(df.groupby("category")["price"].agg(["mean","sum","max"]))





#BAI 5 Merge/Join nhieu bang du lieu
#Trong thực tế, dữ liệu thường nằm ở nhiều bảng khác nhau 
# (giống nhiều table trong database), 
# cần ghép lại để phân tích. pd.merge() 
# giống hệt JOIN trong SQL.
# orders = pd.DataFrame({
#     "order_id": [1, 2, 3, 4],
#     "customer_id": [101, 102, 101, 103],
#     "amount": [500000, 200000, 300000, 700000]
# })

# customers = pd.DataFrame({
#     "customer_id": [101, 102, 103],
#     "name": ["Nam", "Lan", "Huy"]
# })

# # Ghép 2 bảng theo cột chung "customer_id"
# result=pd.merge(orders,customers,on="customer_id")
# print(result)

# #Các loại join (how=) — giống hệt SQL:
# pd.merge(orders, customers, on="customer_id", how="inner")   # mặc định — chỉ giữ dòng khớp ở CẢ 2 bảng
# pd.merge(orders, customers, on="customer_id", how="left")    # giữ TOÀN BỘ bảng trái (orders), bảng phải thiếu thì để NaN
# pd.merge(orders, customers, on="customer_id", how="right")   # giữ TOÀN BỘ bảng phải (customers)
# pd.merge(orders, customers, on="customer_id", how="outer")   # giữ TẤT CẢ dòng ở cả 2 bảng

# #inner: chỉ lấy dữ liệu khớp ở cả 2 bên (hay dùng nhất)
# #left: ưu tiên giữ hết bảng bên trái, dù bên phải không có dữ liệu khớp (sẽ ra NaN)
# #Ví dụ dễ hiểu:
# # orders có đơn hàng của khách 104 (không có trong customers) 
# # → dùng how="left" thì đơn hàng đó vẫn hiện ra, cột name sẽ là NaN. 
# # Dùng how="inner" thì đơn hàng đó bị loại bỏ luôn.

# #Nếu 2 bảng có tên cột khác nhau (vd: bảng 1 là customer_id, bảng 2 là id):
# pd.merge(orders, customers, left_on="customer_id", right_on="id")

#BAI TAP
products = pd.DataFrame({
    "product_id": [1, 2, 3, 4],
    "product_name": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "price": [15000000, 200000, 500000, 3000000]
})

sales = pd.DataFrame({
    "sale_id": [1, 2, 3, 4, 5],
    "product_id": [1, 2, 1, 3, 5],
    "quantity": [2, 5, 1, 3, 2]
})
#(Lưu ý: product_id = 5 trong sales không tồn tại trong bảng products)
#cau 1
print(pd.merge(products,sales,on="product_id",how="inner"))

#cau 2
print(pd.merge(sales,products,on="product_id",how="left"))

#cau 3
merged = pd.merge(products,sales,on="product_id",how="inner")
merged["total_amount"]=merged["price"]* merged["quantity"]
print(merged)


# #BAI 6 Đọc dữ liệu từ file CSV/Excel thật
# #Đọc file CSV
# df = pd.read_csv("products.csv")
# print(df)

# #Đọc file Excel (cần cài thêm thư viện openpyxl):
# # Cài đặt (chạy 1 lần trong terminal): pip install openpyxl
# df = pd.read_excel("products.xlsx")
# print(df)

# #Đọc CSV với 1 số tùy chọn hay dùng:
# df = pd.read_csv("products.csv", encoding="utf-8")   # chỉ định encoding (tránh lỗi font tiếng Việt)
# df = pd.read_csv("products.csv", sep=";")             # nếu file dùng dấu ; thay vì , để phân tách cột
# df = pd.read_csv("products.csv", usecols=["product", "price"])   # chỉ đọc 2 cột cần thiết

# #Ghi DataFrame ra file (ngược lại — xuất dữ liệu đã xử lý):
# df.to_csv("output.csv", index=False)      # index=False để không ghi thêm cột số thứ tự thừa
# df.to_excel("output.xlsx", index=False)

#Kết hợp với csv module đã học ở Bài 7 (Python):
#Bài 7 Python: đọc/ghi CSV bằng module csv — cách "thủ công",
#  đọc từng dòng như list/dict.
#Pandas read_csv: đọc toàn bộ file thành 1 bảng DataFrame ngay lập tức — nhanh hơn,
#  tiện hơn rất nhiều
#  khi cần xử lý dữ liệu lớn (lọc, groupby, merge...).

#→ Trong thực tế Data Engineering,
#  hầu như luôn dùng pd.read_csv() 
# thay vì module csv thủ công, 
# trừ khi cần xử lý từng dòng 1 cách đặc biệt.

#BAITAP
#cau 1
data = {
    "product": ["Laptop", "Mouse", "Keyboard"],
    "price": [15000000, 200000, 500000]
}
df=pd.DataFrame(data)
df.to_csv("my_product.csv",index=False)

#cau 2
df2 = pd.read_csv("my_product.csv")
print(df2)

#cau 3
expensive = df2[df2["price"]>300000]
print(expensive)
expensive.to_csv("expensive_product.csv",index=False)