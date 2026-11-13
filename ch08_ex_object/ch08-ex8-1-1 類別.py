# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 09:11:45 2026

@author: user
"""

# =============================================================================
# 題目：設計寵物登記系統 (類別與物件)
# 你是一家寵物店的店員，請幫每隻寵物建立資料卡，內容包含：`name`（名字）、`species`（種類）。
# 建立 3 隻不同寵物物件，並印出它們的名字與種類。
# =============================================================================

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

dog = Pet("旺財", "狗")
cat = Pet("咪咪", "貓")
bird = Pet("阿呆", "鳥")

print(f'寵物名: {dog.name}, 種類: {dog.species}')
print(f'寵物名: {cat.name}, 種類: {cat.species}')
print(f'寵物名: {bird.name}, 種類: {bird.species}')
