# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 09:58:06 2020

@author: USER
"""

import random
num=random.randint(1,20)
x=input("輸入數字:")
x=int(x)
if x<=0 or x>20:
    print("!輸入錯誤!")
elif x==num:
    print("bingo")
else:
    print("你猜錯了")