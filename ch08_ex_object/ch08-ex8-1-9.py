'''
8-1-9：組合

# 題目：打造自訂機器人！
# 每個 `Robot` 組合一個 `Arm`，用 `show_arm()` 方法介紹手臂。

# arm = Arm(type="鐵製", function="舉重")
# bot = Robot("RX-78", arm)
# bot.show_arm()
# RX-78 擁有一隻鐵製的手臂，功能是舉重

'''

class Arm:
    def __init__(self, type, function):
        self.type = type
        self.function = function
    

class Robot:
    def __init__(self, name, arm):
        self.name = name
        self.arm = arm
        
    def show_arm(self):
        print(f'{self.name} 擁有一隻{self.arm.type}的手臂，功能是{self.arm.function}')

arm = Arm(type="鐵製", function="舉重")
bot = Robot("RX-78", arm)
bot.show_arm()