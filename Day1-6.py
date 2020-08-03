# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 15:21:07 2020

@author: USER
"""

m=input("數學成績:")
e=input("英文成績:")
m=int(m)
e=int(e)
if m>=90 and e>=90:
    print("有獎品")
elif m>=90 or e>=90:
    print("再加油")
else:
    print("要懲罰")
