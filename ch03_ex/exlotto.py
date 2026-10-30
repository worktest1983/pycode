# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 09:22:41 2026

@author: user
"""

import random

# =============================================================================
# My code
# =============================================================================

# def lotto(n,m):
#     return random.sample(range(1, n + 1), m)


# =============================================================================
# Teacher's code
# =============================================================================

def lotto(n,m):
    # 建立一個空的串列
    prize = list()
    
    nums = [i for i in range(1, n+1)]
    
    for i in range(m):
        # 從nums序列中隨機取的一個號碼
        n = random.choice(nums)
        # 將取得的號碼塞到prize串列裡
        prize.append(n)
        # 將剛剛抽取到的號碼刪除掉
        nums.remove(n)
        
    return prize