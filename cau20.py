# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 19:45:40 2024

@author: ACER
"""

a = int(input("Nhao vao so a: "))
b = int(input("Nhap vao so b: "))
c = int(input("Nhap vao so c: "))
if a >= b and a >= c:
    So_lon_nhat = a
elif b >= a and b >=c:
    So_lon_nhat = b
else:
        So_lon_nhat = c
print("So lon nhat la: ", So_lon_nhat)

    
    
    
        