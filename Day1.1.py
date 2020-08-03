# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:56:40 2020

@author: USER
"""

x=input("身高(m):")
y=input("體重(kg):")
x=float(x)
y=int(y)
BMI=y//x**2
if BMI<18.5:
    print("體重不足")
elif BMI<24:
    print("正常")
elif BMI<27:
    print("過重")
elif BMI<30:
    print("輕度肥胖")
elif BMI<35:
    print("中度肥胖")
else:
    print("重度肥胖")
    