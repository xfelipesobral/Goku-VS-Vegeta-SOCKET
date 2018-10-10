from classes import *


#!/usr/bin/env python
# -*- coding: utf-8 -*-

from dados import *
import math

def distancia(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

'''
## ATK -> PERSONAGEM :: DANO()
## PERSONAGEM -> PERSONAGEM :: SE AFASTAM
'''
##def colidirem(personagem):


def mover_jogo(jogo):
    # if((p1.vida == 0) or (p2.vida == 0)):
    
    # if colidirem()

    if jogo.game_ganho:
        jogo.game_ganho = True
        return jogo 
    else:
        jogo.p1.mover()
        jogo.p2.mover()

    return jogo
