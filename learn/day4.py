# i=1
# while i<=5 :
#     print ( i)
#     i=i+1
# print("done!")

# i=1
# while i<=5 :
#     print ('*' * i)
#     i=i+1
# print("done!")

# bi_mat=9
# so_lan_thu=1
# win=False
# while so_lan_thu <=3:
#     so_doan=int(input("Ban doan so may: "))
#     if so_doan == bi_mat:
#         print("Ban da dung")
#         win=True
#         break
#     else:
#         so_lan_thu +=1
# if win == False:
#     print("Ban fail rui !")

# GAME DIEU KHIEN XE OTO 
# cmd=""
# while cmd.upper()!="EXIT" :
#     cmd=input(">") .upper() # dung upper tren nay chi can 1 lan o duoi se tu hieu
#     if cmd=="HELP" :
#         print("""
#         >start: khoi dong xe
#         >stop: dung xe
#         >help: ho tro
#         >exit: thoat chuong trinh
#         """)
#     elif cmd=="START" :
#         print("khoi dong xe")
#     elif cmd=="STOP" :
#         print("Dung xe")
#     else : 
#         print("nhap sai lenh moi nhap lai")


# cmd=""
# start= False # xe luc dau o trang thai stop
# while True :
#     cmd=input(">") .upper() # dung upper tren nay chi can 1 lan o duoi se tu hieu
#     if cmd=="HELP" :
#         print("""
#         >start: khoi dong xe
#         >stop: dung xe
#         >help: ho tro
#         >exit: thoat chuong trinh
#         """)
#     elif cmd=="START" :
#         if start==True :
#             print(" xe da khoi dong rui nhe")
#         else:
#             print("Khoi dong xe")
#             start=True
#     elif cmd=="STOP" :
#         if not start:
#             print("Xe da stop rui nhe")
#         else:
#             print("Dung xe")
#             start=False
#     elif cmd=="EXIT" :
#         break
#     else:
#         print("nhap sai rui moi nhap lai: ")


# VONG LAP FOR
# for chu_cai in "Python":
#     print(chu_cai)

# for hoa_qua in ["Cam","Quyt","Mit"] :
#     print(hoa_qua)

# for so in range(1,10):
#     print(so)

# #in le
# for so in range(1,10,2):
#     print(so)

# #in chan
# for so in range(0,10,2): #(tu,den,buoc nhay)
#     print(so)

# gio hang mua cac mon co gia duoc liet ke
gia_gio_hang=[10,25,30,37]
tong=0
for gia in gia_gio_hang:
    tong+=gia
print(f'Gia tien da mua la:  US{tong}' )


#2 vong for long nhau
# for x in [1,2,3]:
#     for y in [4,5,6]:
#         print(f'({x},{y})')

for x in[5,2,3,7,2,4]:
    for y in "$":
        print(x*y)