# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:30:19 2026

@author: user
"""

# =============================================================================
#  Python CH3 綜合實作專題
# 【大航海時代：神奇酒館決鬥場】專案實作指南
# =============================================================================


from tavern_games import roulette, duel
import announcer as spk

spk.speak("歡迎來到黑鬍子酒館！準備好賭上你的海賊榮耀了嗎？")

def run_game():
    # 自動進行 1 輪輪盤賭博（玩家押注 "紅"）並播報結果
    msg1 = roulette.spin_roulette("紅")
    spk.speak(msg1)
    
    # 自動進行 1 輪武器決鬥並播報結果
    msg2 = duel.weapon_clash()
    spk.speak(msg2)


if __name__ == '__main__':
    run_game()
