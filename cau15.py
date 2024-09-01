# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 15:04:45 2024

@author: ACER
"""


a = int(input("Nhap vao so a: "))
b = int(input("Nhap vao so b: "))
Tinh_bieu_thuc = (((a+b) / ((a)**(1/3)+((b)**(1/3)))) - (a*b)**(1/3)) / ((((a**(1/3)) - (b**(1/3))))**2)
print("Ket qua", Tinh_bieu_thuc)