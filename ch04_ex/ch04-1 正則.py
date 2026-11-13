"""
實作練習 1：格式驗證器
題目：請撰寫一程式，驗證使用者輸入的是否為標準的「台灣統一編號」（八位純數字）。
若正確，顯示「格式合法」。
若含有英文字母或長度不對，顯示「格式不符」。
"""

import re

tax_id = input("請輸入統編: ")

id_match = r"\d{8}"

if re.fullmatch(id_match, tax_id):
    print("格式合法")
else:
    print("格式不符")
    
# 用match要在正則結尾加上$
id_match = r"\d{8}$"

if re.match(id_match, tax_id):
    print("格式合法")
else:
    print("格式不符")    
