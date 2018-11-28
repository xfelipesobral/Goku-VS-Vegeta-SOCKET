#!/usr/bin/env python
# -*- coding: utf-8 -*-

from game.universe import *
import random

'''
====================
 TELA E CONSTANTES
====================
'''

(LARGURA, ALTURA) = (800, 640)
TELA = pg.display.set_mode((LARGURA, ALTURA))

try:
    IMG_P1 = pg.image.load('images/p1.png')
    IMG_P2 = pg.image.load('images/p2.png')
    IMG_BACKGROUND = pg.image.load('images/bg.png')

except:
    IMG_P1 = pg.Surface((100,100),pg.SRCALPHA)
    IMG_P2 = pg.Surface((100,100),pg.SRCALPHA)
    IMG_BACKGROUND = pg.Surface((100,100),pg.SRCALPHA)
    print("IMAGENS NÃO CARREGADAS!!!")

DX = 3

PAREDE_ESQUERDA = 0
PAREDE_DIREITA = LARGURA
PAREDE_CIMA = 0
PAREDE_BAIXO = ALTURA