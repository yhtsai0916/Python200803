# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:26:51 2020

@author: USER
"""

x=input("請輸入成績:")
x=int(x)
if x>=0:
    print("你的等級是:")
    if x>100:
        print("!輸入錯誤!")
    elif x>=90:
        print("A")
    elif x>=80:
        print("B")
    elif x>=70:
        print("C")
    elif x>=60:
        print("D")
    else:
        print("F")