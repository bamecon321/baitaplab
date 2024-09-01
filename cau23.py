# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 14:55:51 2024

@author: ACER
"""

a = float(input("Nhap vao so a: "))
b = float(input("Nhap vao so b: "))
c = float(input("Nhap vao so c: "))
delta = b*b - 4*a*c
if delta < 0:
    print("Phuong trinh vo nghiem")
elif delta == 0:
    print("Phuong trinh co 1 nghiem kep: x1 = x2 = ", -b/(2*a))
else: import math
x1 = (-b + math.sqrt(delta)) / (2*a)
x2 = (-b - math.sqrt(delta)) / (2*a)
print("Phuong trinh co 2 nghiem phan biet: ")
print("x1 = ", x1, "x2 = ", x2)

