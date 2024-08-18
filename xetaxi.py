# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:55:33 2024

@author: ADM
"""
#nhập số km đã đi 
km = float(input("số km mà bạn đã đi là: "))
if km <= 1 :
    m = km*20
elif km <= 3:
    m = km*13
elif km <= 8:
    m = 13*3 + (km-3)*12
else:
    m = 3*13 + 5*12 + (km-8)*10
if m > 100:
    m =m*0.92
print(f"số tiền phải trả là {m}k ")