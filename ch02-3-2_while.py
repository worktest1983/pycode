# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 13:10:51 2026

@author: user
"""

# =============================================================================
# 課堂即時練習 2-3-2 while 迴圈
# 【題目】存款達標模擬器
# 【任務描述】
# 假設初始存款為 1000 元，每月存入 500 元。
# 請使用 while 迴圈計算並印出「需要幾個月」存款才會達到或超過5000 元
# =============================================================================

deposit = 1000
print(f"初始存款為: {deposit}")
print("每月存入500元")

month = 0

while deposit < 5000:
    deposit += 500
    month += 1
    
    # print(f"第{month}月，存款餘額{deposit}元")   

print(f"需要{month}個月，存款才會達到或超過{deposit}元")

# =============================================================================
# # 【職場實務：智慧化庫存控制系統】
# stock_quantity = 50
# print(f"系統啟動。初始庫存：{stock_quantity} 單位")
# 
# # 安全庫存水位為 10，只要庫存大於 10 就繼續運作
# while stock_quantity > 10:
#     print(f"\n目前庫存安全：{stock_quantity}")
#     try:
#         user_buy = int(input("請輸入客戶購買數量 (輸入 0 強制終止)："))
#         if user_buy == 0:
#             print("管理員手動終止系統。")
#             break # 強制跳出迴圈
#         if user_buy <= stock_quantity:
#             stock_quantity -= user_buy # 複合賦值：更新狀態，避免無限迴圈
#             print(f"交易成功！庫存減少為：{stock_quantity}")
#         else:
#             print(f"【警示】庫存不足！現有數量：{stock_quantity}")
#     except ValueError:
#         print("請輸入有效的整數數字。")
#         
#  print("系統提示：庫存低於安全水位，請立即進貨。")
# =============================================================================
