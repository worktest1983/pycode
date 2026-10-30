# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:41:43 2026

@author: user
"""


import random

def weapon_clash():
    weapons = ['佩刀', '火繩槍', '水手西洋劍']
    
    player = random.choice(weapons)    
    enemy = random.choice(weapons)
    
    # 規則 佩刀 勝 水手西洋劍、水手西洋劍 勝 火繩槍、火繩槍 勝 佩刀
    win_rules = {
        "佩刀": "水手西洋劍",
        "水手西洋劍": "火繩槍",
        "火繩槍": "佩刀",
    }
    
    if player == enemy:
        msg = '雙方武器相同，平手'
    
    # 如果玩家武器所對應的勝利對象，剛好就是敵人的武器，那麼玩家獲勝
    elif win_rules[player] == enemy: 
        msg = '玩家獲勝'
    else:
        msg = '玩家失敗'
    
    return (player, enemy, msg)


# =============================================================================
#     # 老師elif的寫法
#     elif (player == '佩刀' and enemy == '水手西洋劍') or \
#          (player == '水手西洋劍' and enemy == '火繩槍') or \
#          (player == '火繩槍' and enemy == '佩刀'):
#              msg = '玩家獲勝'
# =============================================================================



