# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 14:37:28 2026

@author: user
"""

# =============================================================================
# 【情境說明】
# 地球防衛隊收集到了兩組在基地出入的人員名單（有人進出了多次，所以名字有重複）。
# 隊長登記的白名單：["張三", "李四", "王五", "張三", "趙六"]
# 紅外線掃描器錄到的名單：["李四", "王五", "神祕外星人X", "趙六", "李四"]
# 【你的任務】
# 利用 Set（集合）不重複與集合運算（交集、差集）的特性來破案：
# 請將兩組名單轉換為 Set，藉此自動去除重複的名字，並印出乾淨的兩組集合。
# 找出同時出現在「隊長名單」和「紅外線掃描」中的人員（求交集）。
# 找出到底是誰偷偷溜進基地，卻沒有在隊長的白名單上？（提示：用紅外線掃描的集合減去隊長的集合，即求差集）。
# =============================================================================

captain = ["張三", "李四", "王五", "張三", "趙六"]
scanList = ["李四", "王五", "神祕外星人X", "趙六", "李四"]

# 用Set去除重複的
new_captain = set(captain)
new_scanList = set(scanList)
print(f'乾淨的隊長白名單集合: {new_captain}')
print(f'乾淨的紅外線掃描集合: {new_scanList}')
print('-' * 40)


# 計算交集
both = new_captain &  new_scanList
# both = new_captain.intersection(new_scanList)
print(f'同時出現的人員(交集): {both}')
print('-' * 40)


# 計算差集
# spy = new_scanList - new_captain
spy = new_scanList.difference(new_captain)
print(f'偷偷溜進基地的是(差集) : {spy}')