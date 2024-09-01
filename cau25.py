# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 15:32:10 2024

@author: ACER
"""

ch = input("Nhập một chữ cái: ")
if ch.islower():
    ch = ch.upper()
else:
    ch = ch.lower()
print("Kết quả:", ch)
