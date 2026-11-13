'''
題目：動物園計數器 & 公告機
類別變數 total_animals
@classmethod 顯示動物總數
@staticmethod 印出公告。
'''


class zoo:
   
    total_animals = 0    # 只要是透過zoo進來的物件都共用這個變數
    
    def __init__(self):
        zoo.total_animals += 1
        
    def kill(self):
        zoo.total_animals -= 1
    
    @classmethod # 類別方法
    def show_total(cls):
        print(f'現在有{cls.total_animals}隻動物')
        
    @staticmethod  # 靜態方法 (確保不管呼叫方法，不會出現錯誤)
    def post(msg):
        print(f'公告: {msg}')
        

zoo.post('今日園區開放時間 8:00 ~ 17:00 祝各位旅客玩得愉快')
zoo.show_total()
        
p1 = zoo()
p2 = zoo()
p3 = zoo()
zoo.show_total()
zoo.post('請勿餵食園內動物，以免造成動物生病或過胖')

p1.kill()
zoo.show_total()
