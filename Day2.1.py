# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:48:27 2020

@author: USER
"""

import random
num=random.randint(1,20)
i=0
while i<5:
    x=input("輸入數字:")
    x=int(x)
    if x<=0 or x>20:
        print("!輸入錯誤!")
    elif x>num:
        print("小一點")
    elif x<num:
        print("大一點")
    else:
        print("bingo")
    i=i+1
if x!=num:
    print("\n輸了")

    
        
