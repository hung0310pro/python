#!/usr/bin/env python

a = [[n, n*1, n*2, n*5] for n in range(1,4)]
print(a) # [[1, 1, 2, 5], [2, 2, 4, 10], [3, 3, 6, 15]] n di tu 1 den 3 (nho hon 4)

# + list co the in ra nhung cai tk dang tap hop nhu mang, chuoi..

a = list('Hunglm')
print(a) # ['H', 'u', 'n', 'g', 'l', 'm']
a = list([1, 2, 3]) # giong [1, 2, 3] ma k can co list
print(a)

b = [1, 2]
c = b + [3, 4] + ['hun', 'sa', 'lo']
print(c) # [1, 2, 3, 4, 'hun', 'sa', 'lo'] 1 list + vs 1 list cung kieu ms dc

# + kiem tra 1 bien co trong mang hay k
b = [1, 2]
c = 1 in b
print(c) # true

# + lay nhung gia tri trong mang
c = [1, 2, 3, [4, 5], 6 ,7]
print(c[-1]) # 7 lay dc phan tu cuoi
print(c[0]) # lay phan tu dau tien
print(c[1:5]) # [2, 3, [4, 5], 6] lay dc nhung tk co key tu 1 cho den  5 - 1
print(c[1:]) # [2, 3, [4, 5], 6, 7] lay dc nhung tk co key tu 1 cho den het
print(c[:4]) # [1, 2, 3, [4, 5]] lay dc nhung tk co key tu dau cho den  4 - 1


# + khi ca 2 mang cung dung chung 1 bo nho
a = [1, 2, 3]
b = a
b[0] = 'ccc'
print(a) # ['ccc', 2, 3] do 2 tk a va b cung dung chung 1 bo nho nen khi 1 trong 2 
#tk thay doi thi tk con lai thay doi theo (khac php)
print(b) # ['ccc', 2, 3]
# + neu k muon thay doi nhu tren thi chi can de b = list(a) la dc
# + tuy nhien neu nhu truong hop duoi day se van bi thay doi a theo b : 
a = [[1, 2, 3], [1, 2, 3]] 
b = list(a)
print(b) # [[1, 2, 3], [1, 2, 3]]
print(a) # [[1, 2, 3], [1, 2, 3]]

b[0] = 55  # thay doi phan tu con cua mang thi se k thay doi tk mang a
print(b) # [55, [1, 2, 3]]
print(a) # [[1, 2, 3], [1, 2, 3]]

a = [[1, 2, 3], [1, 2, 3]] 
b = a
b[0][0] = 55 # thay doi phan tu con cua mang "con" thi se bi thay doi nhu bt ca b lan a
print(b) # [[55, 2, 3], [1, 2, 3]]
print(a) # [[55, 2, 3], [1, 2, 3]]

# + count : dem so xuat hien cua 1 phan tu trong mang nhu tk chuoi 
# + index : tra ve key cua gia tri trong mang (chuoi cx the)
# + extend : them phan tu vao mang 
a = [1, 2, 3]
a.extend([4, 5, [6, 8]])
print(a) # [1, 2, 3, 4, 5, [6, 8]]

# + clear : xoa phan tu trong mang
# + append : cx them phan tu vao mang nhung "khac tk extend"
a = [1, 2, 3]
a.append([1 , 2, [4, 5]])
print(a) # [1, 2, 3, [1, 2, [4, 5]]]
 
# + copy : copy ra 1 mang y het tk cu nhung mang moi k dung chung "bo nho" vs mang cu
# nen khi 1 phan tu trong mang moi or cu thay doi thi mang con lai cx k bi thay doi
a = [1, 2, 3]
c = a.copy()
c[0] = 11
print(a) # [1, 2, 3]
print(c) # [11, 2, 3] 

# + insert(4, 9) : insert gia tri 9 vao mang tai vi tri la 4
# + pop(1) : bo di phan tu co key  = 1 vi du c = a.pop(1) thi c se bang gia tri cua tk tai vi tri  = 1,
# neu nhu k co phan tu nao chuyen vao thi mac dinh lay phan tu cuoi cung cua mang
# + remove(1) : xoa phan tu co gia tri bang 1 trong mang(chi xoa 1 phan tu dau tien)
# + revert : tao thanh 1 mang bi dao ng
# + sort : sap xep mang, neu sort(reverse=true) thi se sort thi tang dan, con false thi ngc lai
a = [5, 9, 1, 3]
a.sort(reverse=False) # bat buoc la reverse
print(a)