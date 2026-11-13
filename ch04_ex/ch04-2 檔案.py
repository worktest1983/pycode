'''
實作練習 2：自動日誌紀錄器
題目：撰寫一個小程式，每次執行時會詢問使用者的「心情狀態」，
並將「當前時間 + 心情內容」續寫到一個名為 mood_log.txt 的檔案中。
'''

import datetime

today_status = input("今天心情如何? ")

# 取得當前時間，並格式化成 年/月/日 時:分:秒 (strftime)
now = datetime.datetime.now()
current_time = now.strftime('%Y/%m/%d %H:%M:%S')


with open("mood_log.txt", "a", encoding="utf-8", newline="") as d:
    
    text = f"{current_time} {today_status}\n"
    
    d.write(text)
    

print("已成功紀錄你的心情!")    