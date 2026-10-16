# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 11:13:55 2026

@author: user
"""

# =============================================================================
# 課堂即時練習 2-2-3  多向選擇 (if-elif-else)
# 【題目】商品折扣等級計算 
# 【任務描述】
# 請撰寫程式輸入商品單價。
# 單價 5000 以上打 8 折；3000 以上打 9 折；其餘不打折。最後印出「折扣後單價」。
# =============================================================================

original_price = float(input("請輸入商品單價: "))

if original_price > 5000:
    discount_price = original_price * 0.8
elif original_price > 3000:
    discount_price = original_price * 0.9
else:
    discount_price = original_price
    

print(f'折扣後單價 {discount_price}')
    
    
# =============================================================================
# # 【職場實務：企業稅率計算與階梯利潤核發】
# # 接收數據並進行防錯轉換（Defensive Programming 意識）
# try:
#     revenue = float(input("請輸入部門本季營業額 (單位：萬元)："))
# except ValueError:
#     print("輸入格式錯誤，系統將預設為 0。")
#     revenue = 0
#     
# # 建立判斷結構：注意順序必須「由大到小」
# if revenue > 500:
#     bonus_rate = 0.15
#     tier = "頂尖 (Platinum Tier)"
# elif revenue > 300:
#     bonus_rate = 0.10
#     tier = "優良 (Gold Tier)"
# elif revenue > 100:
#     bonus_rate = 0.05
#     tier = "穩定 (Silver Tier)"
# else:
#     bonus_rate = 0.02
#     tier = "基礎 (Bronze Tier)"
#     
# actual_bonus = int(revenue * bonus_rate * 10000) # 換算回新台幣並取整數
# print(f"\n部門評級結果：{tier}")
# print(f"依據級距 {bonus_rate*100}% 計算，本季獎金總額為：{actual_bonus} 元")    
# =============================================================================
