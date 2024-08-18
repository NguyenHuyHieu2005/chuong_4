# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 19:28:33 2024

@author: ADM
"""
#Nhập điểm GPA
a = float(input("Nhập điểm GPA của bạn: "))
#kiểm tra điểm 
if a < 3.5:
    print("Học lực kém")
    
elif  3.5 <= a < 5.0:
    print("Học lực trung bình")
    
elif 5.0  <= a < 7.0:
    print("Học lực khá")
    
elif 8.0 <= a < 9.0:
    print("Học lực giỏi")
    
elif 9.0 <=  a <= 10:
    print("Học lực xuất săc ")
    
else:
    print("không xác định")