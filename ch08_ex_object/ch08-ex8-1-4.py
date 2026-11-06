# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 09:11:45 2026

@author: user
"""

# =============================================================================
# 題目：幫機器狗升級！ (新增參數與方法)
# 加上電量屬性 `battery`，新增 `charge()` 方法印出剩餘電量。
# =============================================================================

class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def speak(self):
        return "我是寵物"

class RobotDog(Pet):
    def __init__(self, name, battery):
        super().__init__('機器' + name, '機器狗')
        self.battery = battery
    
    def speak(Pet):
        return "「汪！我是機器狗，服務至上」"
    
    def charge(self):
        self.battery += 30
        print(f'機器小白正在充電，剩餘電量：{self.battery}%')


robot = RobotDog("小白", battery=50)
robot.charge()

