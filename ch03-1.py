# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 08:56:10 2026

@author: user
"""

# =============================================================================
# 函式
# =============================================================================

def hello(name, age):
    return(f'Hello {name} 您好，{age}歲')
  
name = input('請輸入名字: ')
age = int(input('請輸入年紀: '))

str = hello(name, age)
print(str)

