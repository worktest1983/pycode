# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 09:11:45 2026

@author: user
"""

# =============================================================================
# 題目：變種寵物來了！  (繼承)
# 設計 `RobotDog` 類別繼承 `Pet`，名字前加上「機器」兩字。
# super() 上一層
# =============================================================================

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class RobotDog(Pet):
    def __init__(self, name):
        super().__init__('機器' + name, '機器狗')        

dog = Pet("旺財", "狗")
cat = Pet("咪咪", "貓")
bird = Pet("阿呆", "鳥")
robot = RobotDog("小白")

print(f'寵物名: {dog.name}, 種類: {dog.species}')
print(f'寵物名: {cat.name}, 種類: {cat.species}')
print(f'寵物名: {bird.name}, 種類: {bird.species}')
print(f'寵物名: {robot.name}, 種類: {robot.species}')