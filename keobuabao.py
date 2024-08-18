# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 18:01:31 2024

@author: ADM
"""

import random

# lựa chọn 
choices = ["kéo", "búa", "bao"]

# lựa chọn của ng chơi 
user_choice = input("Nhập lựa chọn của người chơi (kéo, búa, bao): ")

# máy chọn 
computer_choice = random.choice(choices)

# Display the choices
print(f"Bạn chọn: {user_choice}")
print(f"Máy chọn: {computer_choice}")

# tính toán kết quả 
if user_choice == computer_choice:
    print("Hòa!")
elif (user_choice == "kéo" and computer_choice == "bao") or \
     (user_choice == "búa" and computer_choice == "kéo") or \
     (user_choice == "bao" and computer_choice == "búa"):
    print("Bạn thắng!")
else:
    print("Bạn thua!")