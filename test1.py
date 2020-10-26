#!/usr/bin/env python
a = 4
b = 6
print(type(a))
print(type(3.1456221))
print(type('cccccccccc'))

# lay toan bo thu vien cua decimal 
from decimal import*

# lay toi da 30 chu so phan nguyen va phan thap phan cua decimal
getcontext().prec = 30
print (Decimal(10)/Decimal(3)) # 3.33333333333333333333333333333,
print (type(Decimal(10)/Decimal(3))) # decimal.Decimal
# neu doi so 30 thanh 3 thi se show ra la 3.33

from fractions import*
frac = Fraction(6,9)
print(frac) # 2/3 tu rut gon di
print(type(frac)) # fractions.Fraction

