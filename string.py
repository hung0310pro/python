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

