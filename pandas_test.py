#SERIES
import pandas as pd
#prices = pd.Series([100,200,300])
#print(prices)

#DATA FRAME
#Cach tao DATA FRAME tu DICTIONARY
#data={
#    "name" : ["Nam","Lan","Huy"],
#    "salary":[1000,1200,900],
#    "department": ["Engineering", "Sales", "Engineering"]
#}

#df=pd.DataFrame(data)
#print(df)

#df.head()       # xem 5 dòng đầu tiên
#df.tail()       # xem 5 dòng cuối cùng
#df.shape        # xem kích thước (số dòng, số cột) → (3, 3)
#df.columns      # xem tên các cột → Index(['name', 'salary', 'department'])
#df.info()       # xem thông tin tổng quan (kiểu dữ liệu từng cột, có null không...)
#df.describe()   # thống kê nhanh (mean, min, max...) cho các cột số

#lay 1 cot (tra ve SERIES)
#df["name"]        # lấy cột "name"
#df["salary"]       # lấy cột "salary"


#lay nhieu cot(Tra ve DataFrame)
#df[["name","salary"]]

#Lấy 1 dòng theo vị trí (dùng .iloc):
#df.iloc[0]   # lấy dòng đầu tiên (index 0)


#BAI TAP
#cau 1
data ={
   "product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "price": [15000000, 200000, 500000, 3000000],
    "stock": [10, 50, 30, 5]
}
df=pd.DataFrame(data)
print(df)

print(df.shape)
print(df.columns)

#Cau 2
# lay ra cot price tu df
print(df["price"])
#lay 2 cot product va stock cung in ra
print(df[["product","stock"]])
#dung df.iloc de lay dong thu 2 mouse
print(df.iloc[1])


#Lọc dữ liệu theo điều kiện 
# (rất hay dùng — giống WHERE trong SQL):
expensive = df[df["price"]>50000]
print(expensive)
#Giải thích: df["price"] > 500000 trả về 1 Series 
# toàn True/False, rồi df[...] 
# sẽ chỉ giữ lại các dòng có giá trị True.

#Kết hợp nhiều điều kiện 
# (dùng & = và, | = hoặc,
#  mỗi điều kiện phải có ngoặc riêng):

result=df[(df["price"]>50000) & (df["stock"]<20)] 

#Thêm cột mới:
df["total_value"]=df["price"] * df["stock"] # cột mới = giá × tồn kho

#Sửa giá trị 1 cột (áp dụng công thức cho cả cột):
df["price"]=df["price"] *0.9 # giảm giá 10% cho toàn bộ cột price

#Sắp xếp dữ liệu:
df.sort_values("price") # sắp xếp tăng dần theo price
df.sort_values("price",ascending=False) # sắp xếp giảm dần


#BAI TAP
#CAU 1 loc stock <20
low_stock=df[df["stock"]<20]
print(low_stock)
# cau 2 them cot total_value=price*stock
df["total_value"]=df["price"]*df["stock"]
print(df)
#cau 3 sap xep df theo cot price giam dan
print(df.sort_values("price",ascending=False))


#Xử lý dữ liệu thiếu (Missing Data)
#Tạo dữ liệu có giá trị thiếu (dùng None hoặc pd.NA/np.nan):
import pandas as pd
import numpy as np

data={
    "name": ["Nam", "Lan", None, "Huy"],
    "salary": [1000, None, 900, 1200]
}
df=pd.DataFrame(data)
print(df)

#Kiểm tra dữ liệu thiếu:
df.isnull()          # trả về bảng True/False, True = bị thiếu
df.isnull().sum()     # đếm số lượng giá trị thiếu theo từng cột

#Xóa các dòng có giá trị thiếu:
df.dropna()                      # xóa toàn bộ dòng có BẤT KỲ cột nào bị thiếu
df.dropna(subset=["salary"])     # chỉ xóa dòng thiếu ở riêng cột "salary"

#Điền giá trị thay thế cho ô thiếu:
df["salary"] = df["salary"].fillna(0)               # điền 0 vào chỗ thiếu
df["salary"] = df["salary"].fillna(df["salary"].mean())  # điền bằng giá trị trung bình (hay dùng nhất)
df["name"] = df["name"].fillna("Unknown")            # điền chuỗi mặc định

#Trong thực tế, fillna(mean()) 
# hoặc fillna(median()) (giá trị trung vị) 
# hay được dùng cho cột số,
#  vì giúp giữ được xu hướng dữ liệu hơn là điền 0 
# (dễ làm sai lệch phân tích).

#BAI TAP
#Cau 1
data = {
    "product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "price": [15000000, None, 500000, None],
    "stock": [10, 50, None, 5]
}
df=pd.DataFrame(data)
print(df)
print(df.isnull().sum())

#Cau2:dien gia tri thieu o cot price bang gia tri trung binh(mean)
df["price"]=df["price"].fillna(df["price"].mean())
print(df)

#cau 3 xoa cac dong con thieu gia tri o cot stock

print(df.dropna(subset=["stock"]))