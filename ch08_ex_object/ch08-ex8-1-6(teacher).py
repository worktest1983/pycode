'''
題目：動物才藝大賽！
Dog、Bird、Fish 定義 `introduce()` 與 `perform()`，設計 `talent_show(animal)` 看各自才藝。

# 輸出：
# 我是狗狗小黑！現在來表演：汪汪叫！
# 我是小鳥啾啾！現在來表演：高空飛行！
# 我是金魚泡泡！現在來表演：假裝死...
'''
 
class Dog:
    def introduce(self):
        return "狗狗小黑"
    
    def sound(self):
        return "汪汪叫！"

class Bird:
    def introduce(self):
        return "小鳥啾啾"
    
    def sound(self):
        return "高空飛行！"

class Fish:
    def introduce(self):
        return "金魚泡泡"
    
    def sound(self):
        return "假裝死..."


def talent_show(animal):
    print(f'我是{animal.introduce()}！現在來表演：{animal.sound()}')


dog = Dog()
bird = Bird()
fish = Fish()

talent_show(dog)
talent_show(bird)
talent_show(fish)
