# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:08:00 2024

@author: ADM
"""
#nhâp độ dài 3 cạnh 
a = float(input("Nhập độ dài cạnh thứ nhất: "))
b = float(input("Nhập độ dài cạnh thứ hai: "))
c = float(input("Nhập độ dài cạnh thứ ba: "))
if  a*a==b*b+c*c or b*b==a*a+c*c or c*c==b*b+a*a:
    print("đây là tam giác vuông")
elif a==b or b==c:
    print("đây là tam giác đều")
if a==b and  b==c and  c==a:
    print("đây là tam giác cân ")
elif  a*a>b*b+c*c or b*b>a*a+c*c or c*c>b*b+a*a:
    print("đây là tam giác tù")
else:
    print("đây là tam giác thường")