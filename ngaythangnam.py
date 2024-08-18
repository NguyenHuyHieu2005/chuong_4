# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 17:45:12 2024

@author: ADM
"""

 # Nhập vào thời gian theo định dạng dd/mm/yyyy
time_input = input("Nhập vào ngày, tháng , năm (định dạng dd/mm/yy): ")
d , m , y = map(int , time_input.split("/"))
if m < 1 or m> 12:
    print("Không hợp lệ")
else:
    # kiểm tra tháng và ngày 
#tháng có 31 ngày 
    if m in [1, 3, 5, 7, 8, 10, 12]: 
        if d < 1 or d > 31:
            print("Không hợp lệ")
        else:
            print("Hợp lệ")
#tháng có 30 ngày 
    elif m in [4, 6, 9, 11]: 
        if d < 1 or d > 30:
            print("Không hợp lệ")
        else:
            print("Hợp lệ")
#tháng 2 
    elif m == 2:
        if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
            if d < 1 or d > 29:
                print("Không hợp lệ")
            else:
                print("Hợp lệ, tháng này có 29 ngày")
        else:
            if d < 1 or d > 28:
                print("Không hợp lệ")
            else:
                print("Hợp lệ, tháng này có 28 ngày ")
if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    print("Năm này là năm nhuận")
else:
    print("năm này là năm không nhuận")