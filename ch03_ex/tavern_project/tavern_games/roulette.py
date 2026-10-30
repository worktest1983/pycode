# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:41:33 2026

@author: user
"""

import random

def spin_roulette(bet_color):
    # 顏色列表
    list = ['紅', '黑', '綠']
    
    # 隨機顏色
    color = random.choice(list)
    
    if bet_color == color:
        return f'轉出顏色【{color}】, "🎉 恭喜贏得金幣！'
    else:
        return f'轉出顏色【{color}】, "💸 殘念，金幣被酒館收走了！'

