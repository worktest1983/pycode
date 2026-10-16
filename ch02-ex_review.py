# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 15:45:54 2026

@author: user
"""

# =============================================================================
# # 題目來源: CH2_終極實務挑戰.docx
# # 【題目】【星際走私者：黑市太空港自動結帳系統 V3.0】
# # 【題目說明】看檔案
# =============================================================================

# 原始黑市物資價格清單
orignal_price = [4000, 800, 15000, 500, 6200]

# 物品名稱
itmes = {0: "光束粒子砲", 1: "加速推進劑", 2: "反物質核心", 3: "太空乾糧", 4: "隱形匿蹤斗篷"}

# 特價規則 (List Comprehension）
discount_price = [int(p * 0.9) if p > 2000 else p for p in orignal_price]

    
print(">>> 歡迎來到黑市太空港自動結帳系統 V3.0 <<<")
print(f"今日特價資產清單：{discount_price}")

total_bill = 0

# 檢查輸入資料
while True:
    try:    
        buy = int(input("\n請輸入購買商品索引 (0-4),結帳按 -1:"))
        if buy == -1:
            break
        
        if buy < 0 or buy > 4:
            print("【聯邦警訊】查無此物資代碼，請重新輸入！")
            continue
        else:
            total_bill += discount_price[buy]
            print(f"【成功裝載】目前累計金額：{total_bill}")
            
    except ValueError:
        print("【輸入錯誤】請務必輸入整數編號！")
        
# 折扣計算
if total_bill >= 15000:
    total_bill -= 2000
    rating = "梟雄級大宗交易"
elif total_bill >= 8000:
    total_bill -= 800
    rating = "狂徒級買賣"
else:
    rating = "小規模走私"
    
if total_bill > 0 and total_bill % 50 == 0:
    total_bill += 1
    safty_status ="【隱密協定】偵測到聯邦雷達共振！已加收 1 星幣發射干擾誘餌！" 
else:
    msg = ""
    
    
# 輸出明細
print("\n===== 🚀 聯邦邊境星區交易明細 =====")
print(f"交易評級：{rating}")
print(f"安全狀態: {safty_status}")
print(f"【最終應付星幣】：{total_bill} 星幣")
    
    
