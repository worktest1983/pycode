# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 10:53:01 2026

@author: user
"""

# =============================================================================
# My code
# =============================================================================

import random

def invoice():
    
    numbers = [i for i in range(0, 10)]
    prize = ''

    for i in range(8):
        n = random.choice(numbers)
        prize = prize + str(n)
    
    return(prize)
        


# =============================================================================
# Teacher's code
# =============================================================================

def reciept():
    prize2 = ''
    nums = [i for i in range(10)]
    for i in range(8):
        n = random.choice(nums)
        prize2 += str(n)
    return prize2