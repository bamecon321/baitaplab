# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 15:24:48 2024

@author: ACER
"""

gio = int(input("Nhập giờ: "))
phut = int(input("Nhập phút: "))
giay = int(input("Nhập giây: "))
if 0 <= gio <= 23 and 0 <= phut <= 59 and 0 <= giay <= 59:
    print("Thoi gian hop le")
else:
    print("Thoi gian khong hop le")