'''
總練習題：🐉《魔法動物訓練師》
設計一套魔法寵物系統，讓學生整合類別、繼承、多型、例外等概念：
類別 Creature：有 name、power，方法 attack()
類別 Dragon、Phoenix 繼承 Creature，覆寫 attack()
若 power 太低，拋出自訂 TooWeakException
類別 Trainer 擁有多個寵物，方法 train_all() 呼叫每隻攻擊
使用 @classmethod 計算訓練過的寵物總數
加入 @staticmethod 提示玩家：「攻擊會消耗魔力，小心使用！」
'''

