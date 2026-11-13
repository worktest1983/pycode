'''
8-1-7：私有變數

# 題目：保密的魔法名稱
# 巫師類別有私有屬性 `__real_name`，只能用 `reveal()` 方法顯示真名。
# w = Wizard("哈利波特", "哈利‧詹姆士‧波特")
# w.reveal()  # => 真名是：哈利‧詹姆士‧波特
'''

class Wizard:
    def __init__(self, name, realname):
        self.name = name
        self.__real_name = realname
    
    def reveal(self):
        print(f'{self.name}的真名是： {self.__real_name}')
    

w = Wizard("哈利波特", "哈利‧詹姆士‧波特")
w.reveal() 