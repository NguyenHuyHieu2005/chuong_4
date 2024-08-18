# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:02:44 2024

@author: ADM
"""
#nhâp độ dài 3 cạnh 
a = float(input("Nhập độ dài cạnh thứ nhất: "))
b = float(input("Nhập độ dài cạnh thứ hai: "))
c = float(input("Nhập độ dài cạnh thứ ba: "))

#kiểm tra ba cạnh có tạo thành một tam giác hay không 
if a==0 or b==0 or c==0:
    print("một cạnh của tam giác không thể bằng 0 ")
if a+b>c and a+c>b and b+c>a:
    print("a,b,c là 3 cạnh của một tam giác ")
else:
    print("không xác định")
   