'''
設計一套魔法寵物系統，讓學生整合類別、繼承、多型、例外等概念：
1.	類別 Creature：有 name、power，方法 attack()
2.	類別 Dragon、Phoenix 繼承 Creature，覆寫 attack()
3.	若 power 太低，拋出自訂 TooWeakException
4.	類別 Trainer 擁有多個寵物，方法 train_all() 呼叫每隻攻擊
5.	使用 @classmethod 計算訓練過的寵物總數
6.	加入 @staticmethod 提示玩家：「攻擊會消耗魔力，小心使用！」
'''
# =============================================================================
# Creature          寵物名稱、魔力值、攻擊方法  (類別與物件)
# Dragon            龍的火焰攻擊 (繼承、方法覆寫)
# Phoenix           鳳凰的烈焰攻擊 (繼承、方法覆寫)
# TooWeakException  魔力不足時產生例外 (自訂例外)
# Trainer           管理多隻魔法寵物 (物件組合、多型)
# count_trained()   計算訓練寵物總數 (@classmethod )
# show_warning()    顯示魔力使用提醒 (@staticmethod)
# =============================================================================

# 2026-11-13 ChatGPT 

# ==================================
# 1. 自訂例外類別
# ==================================
class TooWeakException(Exception):
    """當寵物魔力不足時產生的例外"""
    pass


# ==================================
# 2. 父類別 Creature
# ==================================
class Creature:

    trained_count = 0  # 記錄訓練過的寵物數量

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        if self.power < 20:
            raise TooWeakException(
                f"{self.name} 魔力不足，無法攻擊！"
            )

        self.power -= 10
        print(f"{self.name} 發動普通攻擊！")
        print(f"剩餘魔力：{self.power}")

    # 類別方法：計算訓練過的寵物總數
    @classmethod
    def count_trained(cls):
        return cls.trained_count

    # 靜態方法：顯示魔力提醒
    @staticmethod
    def show_warning():
        print("攻擊會消耗魔力，小心使用！")


# ==================================
# 3. 子類別 Dragon
# ==================================
class Dragon(Creature):

    def attack(self):
        if self.power < 20:
            raise TooWeakException(
                f"{self.name} 魔力不足，無法使用火焰攻擊！"
            )

        self.power -= 10
        print(f"🐉 {self.name} 發動火焰攻擊！")
        print(f"剩餘魔力：{self.power}")


# ==================================
# 4. 子類別 Phoenix
# ==================================
class Phoenix(Creature):

    def attack(self):
        if self.power < 20:
            raise TooWeakException(
                f"{self.name} 魔力不足，無法使用烈焰攻擊！"
            )

        self.power -= 10
        print(f"🔥 {self.name} 發動鳳凰烈焰！")
        print(f"剩餘魔力：{self.power}")


# ==================================
# 5. Trainer 訓練師類別
# ==================================
class Trainer:

    def __init__(self, name):
        self.name = name
        self.creatures = []

    # 新增寵物
    def add_creature(self, creature):
        self.creatures.append(creature)
        Creature.trained_count += 1
        print(f"成功收服寵物：{creature.name}")

    # 訓練所有寵物
    def train_all(self):
        print(f"\n===== {self.name} 開始訓練 =====")

        for creature in self.creatures:
            try:
                creature.attack()

            except TooWeakException as e:
                print(f"⚠️ 訓練失敗：{e}")


# ==================================
# 6. 主程式
# ==================================

# 顯示攻擊提醒
Creature.show_warning()

# 建立訓練師
trainer = Trainer("小明")

# 建立魔法寵物
dragon = Dragon("火焰龍", 50)
phoenix = Phoenix("不死鳥", 30)
weak_dragon = Dragon("幼龍", 10)

# 收服寵物
trainer.add_creature(dragon)
trainer.add_creature(phoenix)
trainer.add_creature(weak_dragon)

# 訓練所有寵物
trainer.train_all()

# 顯示訓練寵物總數
print("\n訓練過的寵物總數：",
      Creature.count_trained())
