# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 19:56:29 2024

@author: ACER
"""

a = int(input("Nhap vao so a: "))
b = int(input("Nhap vao so b: "))
c = int(input("Nhap vao so c: "))
d = int(input("Nhap vao so d: "))
if a <= b and a <= c and a <= d:
    So_be_nhat = a
elif b <= a and b <= c and b <= d:
    So_be_nhat = b
elif c <= a and c <= b and c <= d:
    So_be_nhat = c
else:
    So_be_nhat = d
print("So be nhat la: ", So_be_nhat)
    