# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 08:58:56 2026

@author: user
"""

# =============================================================================
# class zoo():
#     cnt = 0
#     def __init__(self):
#         zoo.cnt += 1
#     def kill(self):
#         zoo.cnt -= 1
#     @classmethod
#     def show_count(cls):
#         print(f'目前動物園有{cls.cnt}隻動物')
#     @staticmethod
#     def post(s1):
#         print(f'公告:{s1}')
#         
# zoo.post('今日圈開放時間 8:00 ~ 18:00 祝各位旅客玩得愉快')
# zoo.show_count()
# z1 = zoo()
# z2 = zoo()
# z3 = zoo()
# z2.show_count()
# z3.post('請勿餵食園內動物，以免造成動物生病或過胖')
# z1.kill()
# zoo.show_count()
# =============================================================================


# 1. 自訂例外
class TooWeakException(Exception):
    pass


# 2. 基礎類別
class Creature:
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power

    def attack(self):
        pass


# 3. 子類別繼承與覆寫 (多型 + 消耗力量)
class Dragon(Creature):
    def attack(self):
        cost = 25  # 巨龍噴火消耗較多力量
        if self.power < cost:
            raise TooWeakException(f"{self.name} 力量太低 (目前：{self.power}，需要：{cost})，無法噴火！")
        
        damage = self.power * 2
        self.power -= cost  # 攻擊後扣除力量
        print(f"🔥 巨龍 {self.name} 噴出龍息，造成 {damage} 點傷害！(剩餘力量：{self.power})")


class Phoenix(Creature):
    def attack(self):
        cost = 15  # 鳳凰消耗較少力量
        if self.power < cost:
            raise TooWeakException(f"{self.name} 力量太低 (目前：{self.power}，需要：{cost})，無法展翅！")
        
        damage = int(self.power * 1.5)
        self.power -= cost  # 攻擊後扣除力量
        print(f"✨ 鳳凰 {self.name} 俯衝攻擊，造成 {damage} 點傷害！(剩餘力量：{self.power})")


# 4. 訓練師類別
class Trainer:
    total_trained = 0  # 類別屬性：記錄總訓練次數

    def __init__(self, name: str):
        self.name = name
        self.pets = []

    def add_pet(self, pet: Creature):
        self.pets.append(pet)

    @staticmethod
    def show_warning():
        print("💡 提示：攻擊會消耗魔力，小心使用！")

    @classmethod
    def add_trained_count(cls):
        cls.total_trained += 1

    def train_all(self):
        print(f"\n=== 訓練師 {self.name} 開始訓練 ===")
        self.show_warning()
        
        for pet in self.pets:
            try:
                pet.attack()
                self.add_trained_count()
            except TooWeakException as e:
                print(f"⚠️ 訓練失敗：{e}")


# ==========================================
# 測試執行
# ==========================================
if __name__ == "__main__":
    ash = Trainer("小智")
    ash.add_pet(Dragon("史矛革", 40))   # 夠噴 1 次火 (消耗 25，剩 15)
    ash.add_pet(Phoenix("佛客使", 35))  # 夠攻擊 2 次 (消耗 15，剩 20 -> 再消耗 15，剩 5)
    ash.add_pet(Dragon("小火龍", 5))    # 一開始就力量不足

    # 第一輪訓練
    ash.train_all()

    # 第二輪訓練（史矛革會因為上一輪消耗過多，這輪力竭失敗！）
    ash.train_all()

    print(f"\n📊 訓練過的寵物總人次：{Trainer.total_trained}")
