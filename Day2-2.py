# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:21:12 2020

@author: USER
"""

import random
num=random.randint(1,20)
while True:
    x=input("輸入數字:")
    x=int(x)
    if x<=0 or x>20:
        print("!輸入錯誤!")
    while True:
        if x>num:
            print("小一點")
        elif x<num:
            print("大一點")
        else:
            print("bingo")
        break

        
        
    