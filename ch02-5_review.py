# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 14:48:43 2026

@author: user
"""

# =============================================================================
# 【智慧化自動倉儲結帳系統 V2.0】
# 
# 練習目標：綜合運用生成式、while 互動、多向判斷與強健性設計。
# 
# 【練習場景與任務】
# 1. 資料預處理：建立價格清單 [1500, 800, 3200, 450, 2100] ，
# 利用生成式對大於 1000 元 商品進行 85 折「預算處理」。
# 
# 2. 互動購買：利用 while 讓客戶選擇商品索引 (0-4)，輸入 -1 結帳，
# 並包含 try-except 防止輸入錯誤字串。
# 
# 3. 結算優惠：若總額 >= 5000，結帳再折 500 元；若 >= 3000，結帳再折 200 元
# =============================================================================

original_prices = [1500, 800, 3200, 450, 2100]

# 預處理 (對大於 1000 元 商品進行 85 折)
member_prices = [int(p*0.85) if p > 1000 else p for p in original_prices]

print(f">>> 歡迎光臨！今日特價清單：{member_prices}")

total_bill = 0

while True:
    try:
        choice = int(input("\n請輸入購買商品索引 (0-4)，結帳按 -1："))
        
        if choice == -1:
            break
        if 0 <= choice <= 4:
            select_price = member_prices[choice]
            total_bill += select_price
            print(f"【成功加入】目前總累計：{total_bill} 元")
        else:
            print("【警告】無此編號，請重新輸入 0~4 之間的數字。")
    except ValueError:
        print("【輸入錯誤】請務必輸入整數編號！")
        

if total_bill >= 5000:
    total_bill -= 500
    msg = "套用滿 5000 折 500 週年慶優惠"
elif total_bill >= 3000:
    total_bill -= 200
    msg = "套用滿 3000 折 200 滿額禮"
else:
    msg = "未達額外加碼門檻"
    
print("\n===== 最終結帳明細 =====")
print(f"優惠狀態：{msg}")
print(f"【實付總金額】：{total_bill} 元")    
    
