#!/usr/bin/env python
a = """Le
Manh
Hung"""
print(a) # giong nhu la a = "Le \n Manh \n Hung"

'''
nhung cai db
\a : phat ra 1 tieng bip
\n : xuong dong
\b : dua con tro ve lai 1 khoang trang
\t : tao ra 1 tab
\' : in ra ki tu '
\" : in ra ki tu "
\\ : in ra ki tu \
'''

'''
in ra 1 chuoi 5 lan boi *5
aaaaaaa
aaaaaaa
aaaaaaa
aaaaaaa
aaaaaaa
'''
string = "aaaaaaa \n"
print(string*5)


# kiem tra 1 chuoi co nam trong chuoi khac hay k?
strA = "hunglm"
strB = "hu"
strC = strB in strA
print(strC) # True
print(strA[2]) # n
print(strA[2:]) # nglm
print(strA[-1]) # m
print(strA[0:4]) # hung
print(strA[0:None]) # hunglm
print(strA[None:5]) # hungl
print(strA[None:None]) # hunglm

# len() day la ham lay ra do dai cua chuoi
# ep kieu int("9") => 9, str(6) => "6"...


le = 'Le'
hung = f'{le} - aaaaaa'
print(hung)  # Le - aaaaaa

ten = 'Hung'
tuoi = '24'
diaChi = 'Ha Noi'
string = f'Thong tin cua {ten} co tuoi {tuoi} va noi o la {diaChi}'
print(string.center(100, '*')) # Thong tin cua Hung co tuoi 24 va noi o la Ha Noi

#strip giống hàm trim trong php
#replace giống hàm str_replace trong php


hun = "le manh hung"
c = hun.join(['1', '2', '3'])
print(c); # 1le manh hung2le manh hung3


# count dem phan tu trong chuoi

chuoi1 = 'Hung Le Manh eeeeee'
chuoi2 = chuoi1.count('e')
print(chuoi2) # 7

# split tach chuoi thanh 1 mang (nhu ham explode trong php)

# find tim va tra ve vi tri dau tien minh can tim trong chuoi

# isdigit kiem tra 1 tk co phai so hay khong