# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 19:52:23 2024

@author: ADM
"""

#nhập nghiệm 
a = int(input("nhập nghiệm a: "))
b = int(input("nhập nghiệm b: "))
#thực hiện kiểm tra 
if a == 0:
    if b == 0:
        print("phương trình có vô số nghiệm ")
    else:
        print("phương trình vô nghiệm")
else:
    x = -b / a 
    print (f"phương trình có một nghiệm duy nhất là {x}")