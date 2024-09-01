# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 14:56:02 2024

@author: ACER
"""

a = int(input("Nhap vao so a: "))
b = int(input("Nhap vao so b: "))
if a != 0:
    print("Phuong trinh co nghiem x= ", -b/a)
else:
    if b != 0:
        print("Phuong trinh vo nghiem")
    else: print("Phuong trinh vo so nghiem")
    