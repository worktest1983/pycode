# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 09:11:45 2026

@author: user
"""

# =============================================================================
# 題目：讓寵物說話！ (覆寫方法)
# 一般寵物回應：「我是寵物」，機器狗覆寫成：「汪！我是機器狗，服務至上」。
# =============================================================================

# super() 上一層

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def speak(self):
        return "我是寵物"

class RobotDog(Pet):
    def __init__(self, name):
        super().__init__('機器' + name, '機器狗')
    
    def speak(Pet):
        return "「汪！我是機器狗，服務至上」"

dog = Pet("旺財", "狗")
cat = Pet("咪咪", "貓")
bird = Pet("阿呆", "鳥")
robot = RobotDog("小白")

print(f'{dog.name}: {dog.speak()}')
print(f'{cat.name}: {cat.speak()}')
print(f'{bird.name}: {bird.speak()}')
print(f'{robot.name}: {robot.speak()}')