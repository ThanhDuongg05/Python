# # LIST
# name=['Lan','Mai','Nga','Minh']
# name[0]='Nan' # thay cho cua Lan = Nan
# print(name)
# #in phan tu dau tien dung chi so
# print(name[0]) # tu dau (lan)
# print(name[-1])# tu cuoi ( minh)
# print(name[0:-1])# tu A->D

# day_so=[1,9,6,3,28,11]# list
# # tim so lon nhat trong day so tren
# max=day_so[0]
# for i in day_so :
#     if(i>max):
#         max=i
# print(f'{max} la so lon nhat')

# #LIST 2 chieu (Ma tran)
# matrix=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9] 
# ] # la 1 list
# print(matrix[0][1]) # 0 la tuong ung voi cai dong do 1 la tuong ung voi gia tri do

# matrix[2][2]=10 # thay doi gia tri cua 1 phan tu
# print(matrix)
# print(matrix[2][2])

# # dung for de in ma tran
# for hang in matrix:
#     for phan_tu in hang:
#         print(phan_tu)

# # PHUONG THUC TREN LIST
# day_so=[1,6,32,8,9,1]
# #noi cuoi day
# day_so.append(30) # noi them phan tu
# print(day_so)
# #chen vao 1 cho bat ky cua day
# day_so.insert(4,5)# vi tri thu 4 voi gia tri la 5
# print(day_so)
# #xoa 1 gia tri bat ky
# day_so.remove(8) # xoa gia tri
# print(day_so)
# #lay phan tu cuoi cung
# day_so.pop()
# print(day_so)
# #xoa sach danh sach
# # day_so.clear()
# # print(day_so)
# #index biet vi tri cua gia tri do
# print(day_so.index(32))#vi tri thu 2
# print(100 in day_so) # C2:FALSE
# print(9 in day_so) 
# print(day_so.count(1))# dem phan tu gia tri la 1
# day_so.sort()# sap xep day so
# print(day_so) # tang dan
# day_so.reverse() # dao nguoc lai giam dan
# print(day_so)
# day_so2=day_so.copy() # copy day so va co the chinh sua
# print(day_so)
# print(day_so2)

# #BAI TAP VE LIST []
# mang=[1,6,32,6,8,9,1]
# # remove cac phan tu trung lap
# mang_ko_trung=[]
# for i in mang:
#     if i not in mang_ko_trung: # i ko ton tai o day so ko trung thi dc them vao
#         mang_ko_trung.append(i)
# print(mang_ko_trung)

#KIEU DU LIEU TUPLE() ( La mot danh sach nhung khac la ko tac dong 
# duoc vao danh sach nhu LIST (kieu danh sach co dinh))
# ko muon lam thay doi danh sach thi dung kieu nay
# day_so=(1,2,6,8,3)
# day_so[0]=2 # bao loi ngay

#KY THUAT unpacking
# day_so=(1,2,3)
# x=day_so[0]
# y=day_so[1]
# z=day_so[2]
# tich=x*y*z
# print(tich) # qua dai
# # dung unpacking
# x,y,z=day_so
# tich=x*y*z
# print(tich)

#DICTIONARY{}
# sinh_vien={
#     "Ho ten" : "Nguyen thanh duong",
#     "email":"an@gmail.com",
#     "tuoi": "20",
#     "Phone": "0123456",
#     "email2":"an2@gmail.com" 
#     #Key : value (Key ko duoc trung nhau chi value duoc trung nhau)
# }
# print(sinh_vien["Ho ten"])
# print(sinh_vien["email"])
# print(sinh_vien["Phone"]) 
# #hoac dung
# print(sinh_vien.get("NgaySinh")) # dung get se ko bi loi ma no se bao none
# print(sinh_vien.get("NgaySinh","3/3/2020")) # them gia tri vao duoc
# #hoac dung
# sinh_vien["dia chi"]="TP.HCM"
# print(sinh_vien.get("dia chi"))
# #viet tu khoa key ma sai thi se bao loi

#BAI TAP DICTIONARY{}
phone_so=input("Phone:")
chuyen_doi={
    "0":"zero",
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"night"
}
phone_chu="" #chuoi rong
for so in phone_so: # doi voi tung so trong phone so
    phone_chu+=chuyen_doi.get(so,"*")+" " # lay tung ky tu +=o chuyen doi
    #phone chu bang chuyen doi .get(voi so do,"thay doi bang *")
print(phone_chu)