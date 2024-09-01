# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:35:27 2024

@author: ACER
"""

ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))
nam = int(input("Nhập năm: "))

print(f"{ngay}/{thang}/{nam}")

print(f"{ngay}/{thang}/{str(nam)[-2:]}")

print(f"{nam}/{thang}/{ngay}")

ngay, thang, nam = map(int, input("Nhập lại theo định dạng ngày/tháng/năm: ").split('/'))

print(f"{ngay}/{thang}/{nam}")

print(f"{ngay}/{thang}/{str(nam)[-2:]}")

print(f"{nam}/{thang}/{ngay}")
    