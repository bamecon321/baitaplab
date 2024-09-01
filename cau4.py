# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:39:28 2024

@author: ACER
"""

N = int(input("Nhap vao so nguyen duong N co 2 chu so: "))
if 10 <= N <= 99:
    Hang_chuc = N // 10
    Hang_don_vi = N % 10
    Tong_chu_so = Hang_chuc + Hang_don_vi
    print("Ket qua la: ", Tong_chu_so)
else:
    print("Khong phai la so nguyen duong N co 2 chu so")
        