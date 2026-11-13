'''
8-1-8：特殊方法

# 題目：誰是假人？
# 實作 `__eq__` 方法，比較兩個角色是否為同一人（`name` 與 `id_code` 相同）。
# 實作 __eq__ 方法達成以下行為：
# print(char1 == char2)  # True or False
'''

class Character:
    def __init__(self, name, id_code):
        self.name = name
        self.id_code = id_code
        
    def __eq__(self, o):
        return self.name == o.name and self.id_code == o.id_code
        
        
char1 = Character("小白", "3")
char2 = Character("小白", "3")

if char1 == char2:
    print("char1 和 char2為同一個人")
else:
    print("char1 和 char2不是同一個人")