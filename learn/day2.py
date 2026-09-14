#chuoi trong python
# ten="Nguyen Thanh Duong ne con"# dung nay cho TA thi ok hon
# ten='Nguyen Thanh Duong ne con'#hoac nay cung dc
#ten='Chung ta goi "Nguoi ay" la hacker' #nhu nay cung dc
# print (ten)

# viet nhieu dong thi dung (''')
email='''Hello ban
Chung toi cam on anh ve su ho tro vua qua
Tran trong cam on
Cong ty ABC
'''
print(email)


chuoi='ABCDEFGH'
#in chu cai dau tien hoac cac chu cai khac thi them dau []
print(chuoi[1])# ra chu B
print(chuoi[-2])#ra chu G
print(chuoi[0:3]) # in mot day tu A den C vi no loai tru so 3 di
print(chuoi)#ra nguyen dong ki tu
print(chuoi[1:-1])


# ho='Nguyen'
# ten='Thanh Duong'
# print("[" + ho +" "+ ten+']'+" la mot lap trinh vien")


chuoi="Hom nay troi rat dep"
print(len(chuoi)) # kiem tra do dai chuoi (dem)
# ham len kiem tra nhieu kieu nen no duoc goi la ham
print(chuoi.upper()) # in hoa gia tri van giu nguyen
print(chuoi.lower()) # in thuong gia tri van giu nguyen
print(chuoi)
print(chuoi.find('H')) # tim kiem ki tu nao do chu nao ko co no se ra -1
print(chuoi.find('troi'))
print(chuoi.replace('rat dep','trong xanh'))# thay the tu rat dep -> trong xanh ko tim thay thi in chuoi ban dau
#kiem tra chu co nam trong chuoi ko
print('troi' in chuoi) # ton tai in true va ko ton tai in false


#CAC PHEP TOAN DUOC SU DUNG TRONG PYTHON
#ngoai + - * /
#chia lay nguyen : // print(10//3)
# chia lay du : % print(10%3)
# so mu : print(10 ** 3)-> 10^3

# x=10
# x=x+3 hay x+=3 hay x-=3 hay x*=3
# print(x)

#THU TU THUC HIEN PHEP TOAN
# x=10+2*3 # nhan chia truoc cong tru sau
# x=10+2*3**2 mu(1)-> nhan chia(2) -> cong tru (3)
# x=(10+2)*3**2 cong tru(1)->mu(2)->nhan chia(3)
# x= (12+2) *3**2 /2 cong tru(1)->mu(2)->nhan chia(3) ra 63
# print(x)


# CAC HAM TOAN HOC
import math 
# (go python math module ra rat nhiu)
x=2.6
print(round(x))# lam tron
print(abs(-2.6))# tri tuyet doi
print(math.ceil(x)) # tra ve so nguyen ben phai gan nhat
print(math.floor(x)) # tra ve so nguyen ben trai gan nhat