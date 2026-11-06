'''
8-1-6：多型

# 題目：動物才藝大賽！
# Dog、Bird、Fish 定義 `introduce()` 與 `perform()`，設計 `talent_show(animal)` 看各自才藝。

# 輸出：
# 我是狗狗小黑！現在來表演：汪汪叫！
# 我是小鳥啾啾！現在來表演：高空飛行！
# 我是金魚泡泡！現在來表演：假裝死...

'''


class Pet:
    def __init__(self, name):
        self.name = name
        
    def who(self):
        return self.name
        

class Dog(Pet):
    def __init__(self, name):
        super().__init__('狗狗' + name)
    
    def sound(self):
        return "汪汪叫！"

class Bird(Pet):
    def __init__(self, name):
            super().__init__('小鳥' + name)
    
    def sound(self):
        return "高空飛行！"

class Fish(Pet):
    def __init__(self, name):
            super().__init__('金魚' + name)
    
    def sound(self):
        return "假裝死..."


def talent_show(animal):
    print(f'我是{animal.who()}！現在來表演：{animal.sound()}')


dog = Dog("小黑")
bird = Bird("啾啾")
fish = Fish("泡泡")

talent_show(dog)
talent_show(bird)
talent_show(fish)
