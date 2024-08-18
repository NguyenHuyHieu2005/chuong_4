# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 20:09:59 2024

@author: ADM
"""
import math 
#nhập nghiệm 
a = float(input("nhập nghiệm a: "))
b = float(input("nhập nghiệm b: "))
c = float(input("nhập nghiệm c: "))
#thực hiện kiểm tra 
detal = b**2 - 4*a*c
if a == 0:
#nếu a=0 thì đây là phương trình bậc nhất 
    if b == 0:
        if c == 0:
            print("phương trình có vô số nghiệm ")
        else:
            print("phương trình vô nghiệm")
    else:
        e = -c  / b 
        print ("phương trình có một nghiệm duy nhất là " , e  )
if detal < 0: 
    print("phương trình vô  nghiệm ")
elif detal == 0:
     x = -b /(2*a)
     print ("phương trình có nghiệm kép là " , x )
else:
    x1 = (-b + math.sqrt(detal))/(2*a)  
    x2 = (-b - math.sqrt(detal))/(2*a)  
    print("phương trình có hai nghiệm là" , x1 , x2 )