#DIEU KIEN IF
# is_cold=True
# is_hot=True
# if is_cold:
#     print("Troi lanh")
# elif is_hot: #else if
#     print("Troi nong")
# print("Chuc ban vui ve nhe ")

# is_cold=False
# is_hot=False
# if is_cold:
#     print("Troi lanh") # sai thi bo dong nay xun thuc thi dong duoi
# elif is_hot: #else if
#     print("Troi nong")  # sai thi bo dong nay xun thuc thi dong duoi
# else:
#     print("Troi dep")
# print("Chuc ban vui ve nhe ")

# gia_nha=1000000000
# is_cn=True
# if is_cn:
#     giam_gia=0.1*gia_nha #giam 100000000.0
# else:
#     giam_gia=0.12*gia_nha # giam 120000000.0
# print(f'Gia da duoc giam la: {giam_gia} VND')


#CAC PHEP TOAN LOGIC
# AND OR NOT
# thu_nhap=True
# lich_su_tc=True
# co_so_tiet_kiem=True
# no_xau=False
# if thu_nhap and not no_xau:
#     print("Ngan hang cho vay")
# else:
#     print("Ngan hang ko cho vay")

#CAC PHEP TOAN SO SANH
# > || < || >= || <= || == (1 dau bang la phep gan 2 dau bang la so sanh)
nhiet_do=30
if nhiet_do>=30:
    print("troi nong")
elif nhiet_do<30 and nhiet_do>15:
    print("troi mat")
else:
    print("troi lanh")

ten=input("ten ban la gi? ") #input la kieu tu nhap ak
if len(ten) <1:
    print("ten qua ngan")
elif len(ten)>10:
    print("ten qua dai")
else:
    print("ten phu hop")